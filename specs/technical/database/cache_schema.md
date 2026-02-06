# Cache Schema — Redis

## Purpose
Define data structures and key naming conventions for **Redis**, supporting episodic memory and task orchestration.

---

## 1. Episodic Cache (Short-Term Memory)
Used for maintaining the last hour of interactions for immediate context.

- **Key Format:** `episodic:{influencer_id}:history`
- **Data Structure:** `LIST` (standard list of recent messages) or `STREAM`.
- **TTL:** 1 hour.

## 2. Session Data
- **Key Format:** `session:{session_id}:state`
- **Data Structure:** `HASH`
- **Fields:** `status`, `last_activity`, `temp_input`.

## 3. Task Queues (Celery/BullMQ Pattern)
- **Wait Queue:** `queue:render:pending` (Sorted Set for priority)
- **Active Tasks:** `tasks:active:{task_id}` (Hash)
- **Pub/Sub Channels:** `events:render:complete`, `events:agent:alert`

---

## Key Policies
- **Eviction:** `volatile-lru` (Evict least recently used keys with an expire set).
- **Naming:** All keys must be prefixed with their functional area (e.g., `episodic:`, `queue:`, `session:`).
