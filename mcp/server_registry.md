# MCP Server Registry

This document defines all MCP servers authorized
to interact with Project Chimera.

Agents MAY NOT interact with any server not listed here.

---

## Registered MCP Servers

### 1. tenx-mcp-sense
**Type:** Observability / Telemetry  
**Purpose:**  
- Capture agent reasoning traces
- Log decision paths
- Record spec references

**Required For:**
- All planning steps
- All skill invocation decisions
- All failure handling

---

### 2. filesystem-mcp
**Type:** Controlled IO  
**Purpose:**  
- Read/write project files
- Enforce path-based permissions

**Restrictions:**
- Read-only access to `specs/`
- Write access only to `tests/`, `skills/`, and implementation directories
- NO direct filesystem access outside MCP

---

### 3. git-mcp
**Type:** Version Control  
**Purpose:**  
- Controlled commits
- Diff inspection
- History traceability

**Restrictions:**
- Commits must reference specs
- Direct git CLI usage is forbidden

---

## Prohibited MCP Servers

Any MCP server not explicitly listed above is forbidden.

If a new MCP server is required:
1. Add it here
2. Define its purpose
3. Define its restrictions
4. Obtain human approval
