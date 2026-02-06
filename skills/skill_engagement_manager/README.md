# Skill: Engagement Manager

## Skill ID
skill_engagement_manager

## Purpose
Handle and respond to user engagements (comments, mentions, DMs, reactions) across content types: text, audio, video, and images.

This skill primarily responds to inbound engagements and may perform actions typical of human social accounts (reply, react, send DM, attach media), subject to safety constraints and orchestration rules.

This skill does NOT publish original content on its own initiative; actions must be initiated by upstream workflows or Worker Agents.

---

## Allowed Callers
- Worker Agent
- Orchestration Service (authorized modules only)

---

## Notes
- When responding to media (audio/video/image), the `payload` should include `media_url` and optional `caption`.
- For sensitive or high-risk engagements (impersonation requests, alleged copyrighted media, deepfake indicators), the skill will enqueue a human-review ticket and return `human_review_ticket` in the output.
