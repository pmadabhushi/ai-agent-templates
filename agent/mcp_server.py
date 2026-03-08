#!/usr/bin/env python3
"""
Agent Context Kit — MCP Server
================================
Exposes your team's knowledge (personas, skills, design docs) as MCP tools
that any compatible AI tool can use (Kiro, Cursor, VS Code, Claude Desktop, etc.).

This is a lightweight, read-only server. It doesn't run an LLM — it just makes
your agent configuration queryable via the Model Context Protocol.

Usage:
  # Run directly (stdio transport — used by most MCP clients)
  python mcp_server.py

  # Or configure in your AI tool's MCP settings (see below)

Kiro config (.kiro/settings/mcp.json):
  {
    "mcpServers": {
      "agent-context-kit": {
        "command": "python",
        "args": ["path/to/agent/mcp_server.py"],
        "disabled": false,
        "autoApprove": ["list_domains", "list_skills", "list_design_docs"]
      }
    }
  }

Cursor config (.cursor/mcp.json):
  Same format as above.
"""

from __future__ import annotations

from fastmcp import FastMCP

from config import (
    get_domains,
    load_agents_md,
    load_persona,
    load_skill,
    list_skills,
    load_design_docs,
    list_design_docs,
    load_all_skills,
    build_system_prompt,
    SKILL_TRIGGER_MAP,
)

mcp = FastMCP(
    name="agent-context-kit",
    instructions=(
        "This server provides access to structured team knowledge: "
        "personas, AGENTS.md configs, skills (step-by-step runbooks), "
        "and design documents across coding, devops, and security domains. "
        "Use list_domains to discover available domains, then query specific "
        "context as needed."
    ),
)


# ---------------------------------------------------------------------------
# Discovery tools
# ---------------------------------------------------------------------------

@mcp.tool()
def list_domains() -> str:
    """List all available domains with their descriptions and available skills.

    Call this first to discover what's available.
    """
    domains = get_domains()
    lines = []
    for name, config in domains.items():
        skills = list_skills(name)
        design = list_design_docs(name)
        design_summary = ", ".join(
            f"{cat} ({len(docs)})" for cat, docs in design.items()
        ) if design else "none"
        lines.append(
            f"## {name}\n"
            f"- Description: {config['description']}\n"
            f"- Skills: {', '.join(skills)}\n"
            f"- Design docs: {design_summary}"
        )
    return "\n\n".join(lines)


@mcp.tool()
def get_team_config(domain: str) -> str:
    """Get the AGENTS.md configuration for a domain.

    Returns the full team config including build commands, conventions,
    safety rules, and environment info.

    Args:
        domain: The domain to query (coding, devops, security).
    """
    domains = get_domains()
    if domain not in domains:
        return f"Unknown domain: {domain}. Available: {', '.join(domains.keys())}"
    return load_agents_md(domain)


@mcp.tool()
def get_persona(domain: str) -> str:
    """Get the persona definition for a domain.

    Returns the full persona including identity, mindset, methodology,
    safety rules, and output format.

    Args:
        domain: The domain to query (coding, devops, security).
    """
    domains = get_domains()
    if domain not in domains:
        return f"Unknown domain: {domain}. Available: {', '.join(domains.keys())}"
    return load_persona(domain)


# ---------------------------------------------------------------------------
# Skills tools
# ---------------------------------------------------------------------------

@mcp.tool()
def get_skill(domain: str, skill_name: str) -> str:
    """Get step-by-step instructions for a specific skill.

    Skills are runbooks with prerequisites, numbered steps, output format,
    and escalation rules. Load the relevant skill before performing any
    operational task.

    Args:
        domain: The domain (coding, devops, security).
        skill_name: The skill to load (e.g., deploy_service, incident_triage).
    """
    domains = get_domains()
    if domain not in domains:
        return f"Unknown domain: {domain}. Available: {', '.join(domains.keys())}"
    content = load_skill(domain, skill_name)
    if content:
        return content
    available = list_skills(domain)
    return f"Skill '{skill_name}' not found in {domain}. Available: {', '.join(available)}"


@mcp.tool()
def get_all_skills(domain: str) -> str:
    """Get all skills for a domain with their full content.

    Use this when you need the complete skill set loaded at once.

    Args:
        domain: The domain (coding, devops, security).
    """
    domains = get_domains()
    if domain not in domains:
        return f"Unknown domain: {domain}. Available: {', '.join(domains.keys())}"
    all_skills = load_all_skills(domain)
    if not all_skills:
        return f"No skills found for {domain}."
    sections = []
    for name, content in all_skills.items():
        sections.append(f"# Skill: {name}\n\n{content}")
    return "\n\n---\n\n".join(sections)


@mcp.tool()
def match_skill(domain: str, user_message: str) -> str:
    """Find the best matching skill for a user's message based on keyword triggers.

    Use this to determine which skill to load before performing a task.

    Args:
        domain: The domain (coding, devops, security).
        user_message: The user's message or task description.
    """
    triggers = SKILL_TRIGGER_MAP.get(domain, {})
    if not triggers:
        return f"No skill triggers defined for {domain}."

    message_lower = user_message.lower()
    matches = []
    for skill_name, keywords in triggers.items():
        matched_keywords = [kw for kw in keywords if kw in message_lower]
        if matched_keywords:
            matches.append((skill_name, matched_keywords))

    if not matches:
        available = list_skills(domain)
        return f"No skill matched. Available skills for {domain}: {', '.join(available)}"

    # Return best match (most keyword hits) with the skill content
    matches.sort(key=lambda x: len(x[1]), reverse=True)
    best_skill, matched_kw = matches[0]
    content = load_skill(domain, best_skill)

    return (
        f"Matched skill: {best_skill} (keywords: {', '.join(matched_kw)})\n\n"
        f"{content}"
    )


# ---------------------------------------------------------------------------
# Design docs tools
# ---------------------------------------------------------------------------

@mcp.tool()
def get_design_doc(domain: str, category: str, doc_name: str) -> str:
    """Load a specific design document by category and name.

    Args:
        domain: The domain (coding, devops, security).
        category: The design category (e.g., services, architecture, threat_models).
        doc_name: The document name (without .md extension).
    """
    domains = get_domains()
    if domain not in domains:
        return f"Unknown domain: {domain}. Available: {', '.join(domains.keys())}"

    design_docs = load_design_docs(domain)
    if category not in design_docs:
        available = list(design_docs.keys())
        return f"Category '{category}' not found in {domain}. Available: {', '.join(available)}"

    for doc in design_docs[category]:
        if doc["name"].lower() == doc_name.lower():
            return f"# {doc['name']} ({doc['path']})\n\n{doc['content']}"

    names = [d["name"] for d in design_docs[category]]
    return f"Doc '{doc_name}' not found in {category}. Available: {', '.join(names)}"


@mcp.tool()
def search_design_docs(domain: str, query: str) -> str:
    """Search across all design documents for a domain.

    Use this to find specific architecture details, API specs, patterns,
    threat models, policies, or controls.

    Args:
        domain: The domain to search (coding, devops, security).
        query: Text to search for (case-insensitive).
    """
    domains = get_domains()
    if domain not in domains:
        return f"Unknown domain: {domain}. Available: {', '.join(domains.keys())}"

    design_docs = load_design_docs(domain)
    if not design_docs:
        return f"No design docs found for {domain}."

    results = []
    query_lower = query.lower()

    for category, docs in design_docs.items():
        for doc in docs:
            if query_lower in doc["content"].lower():
                # Find matching lines with context
                lines = doc["content"].split("\n")
                matches = []
                for i, line in enumerate(lines):
                    if query_lower in line.lower():
                        start = max(0, i - 1)
                        end = min(len(lines), i + 2)
                        context = "\n".join(lines[start:end])
                        matches.append(f"  Line {i+1}:\n{context}")

                results.append(
                    f"[{category}] {doc['name']} ({doc['path']})\n"
                    + "\n---\n".join(matches[:3])
                )

    if not results:
        return f"No matches for '{query}' in {domain} design docs."

    return f"Found {len(results)} document(s) matching '{query}':\n\n" + "\n\n".join(results)


# ---------------------------------------------------------------------------
# Full context tool (for building system prompts)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_full_context(domain: str) -> str:
    """Get the complete system prompt for a domain.

    Returns the full assembled context: persona + AGENTS.md + all design docs
    + all skills + trigger rules. This is what the agent loads at startup.

    Use this when you need the complete context for a domain in one call.

    Args:
        domain: The domain (coding, devops, security).
    """
    domains = get_domains()
    if domain not in domains:
        return f"Unknown domain: {domain}. Available: {', '.join(domains.keys())}"
    return build_system_prompt(domain)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()
