# Platform Policies — skill_publish_content

## General Rules

- Platform-specific constraints MUST be respected
- Rate limits MUST be enforced
- Rejected content MUST NOT be reattempted automatically
- Metadata manipulation is prohibited

---

## Platform Safety Constraints

### YouTube
- No misleading titles or thumbnails
- Age restrictions must be honored

### TikTok
- Strict rate limits
- Content moderation errors are final

### Twitter / X
- Character limits enforced
- Duplicate posting discouraged

### Instagram
- Media type must match endpoint
- Scheduling subject to platform limits

---

## Failure Classification

- Authentication failure → Non-recoverable
- Rate limiting → Recoverable
- Policy rejection → Safety-critical

Safety-critical failures MUST trigger:
- Governance event
- Possible influencer suspension
