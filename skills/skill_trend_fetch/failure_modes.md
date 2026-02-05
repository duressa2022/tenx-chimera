# Failure Modes — skill_trend_fetch

## Recoverable
- MCP timeout
- Rate limiting

Action:
- Retry (max 3)
- Emit error event

---

## Non-Recoverable
- Invalid input schema
- Unsupported source

Action:
- Immediate failure
- No retry

---

## Safety-Critical
- Trend classified as high risk

Action:
- Return result with risk_level = high
- Caller MUST escalate
