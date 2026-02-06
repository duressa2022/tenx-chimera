# Security Policy — Project Chimera

## Scope

This policy covers:
- Agent behavior
- Skill execution
- External integrations
- Data handling
- Supply chain integrity

---

## Threat Model

Primary risks:
- Rogue agent behavior
- Spec bypass
- Unsafe autonomous actions
- Credential leakage
- Undocumented external access

---

## Security Guarantees

Project Chimera enforces:

- MCP-only external access
- Schema-validated inputs/outputs
- Immutable audit logs
- No direct secret access by agents
- No self-modifying agents

---

## Reporting Vulnerabilities

Security issues MUST be reported responsibly.

Do NOT:
- Open public issues for vulnerabilities
- Commit exploit code
- Test against production credentials

Instead:
- Contact maintainers privately
- Provide reproduction steps
- Reference affected specs

---

## Agent Security Rules

Agents MUST:
- Fail closed
- Log all errors
- Reference specs on failure

Agents MUST NOT:
- Guess
- Retry indefinitely
- Mask failures
- Access undeclared resources

---

## Incident Response

On confirmed security incident:
1. Suspend affected agents
2. Lock irreversible actions
3. Preserve audit logs
4. Escalate to human review

No automated recovery is permitted for security incidents.
