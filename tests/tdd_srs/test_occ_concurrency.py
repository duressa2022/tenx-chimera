import pytest
import time
from concurrent.futures import ThreadPoolExecutor

def test_occ_state_collision_rejection():
    """
    SRS FR 6.1 Requirement: Optimistic Concurrency Control (OCC).
    Verifies that a write attempt with an outdated state_version is rejected.
    """
    from chimera.storage import StateManager
    
    storage = StateManager()
    
    # Phase 1: Two workers read the same state version
    initial_state = storage.get_state("influencer-1")
    v1 = initial_state.version
    
    # Phase 2: Worker A commits successfully
    success = storage.commit_change("influencer-1", expected_version=v1, new_data={"posts": 1})
    assert success is True
    
    # Phase 3: Worker B attempts to commit with the same (now stale) version v1
    # This MUST fail according to the OCC protocol
    try:
        collision_success = storage.commit_change("influencer-1", expected_version=v1, new_data={"posts": 2})
        assert collision_success is False, "OCC failed to detect state collision"
    except Exception as e:
        # Implementation might raise a specific VersionConflictError
        assert "VersionConflict" in str(e)

def test_state_version_increment_on_success():
    """Verifies that every successful commit increments the state_version."""
    from chimera.storage import StateManager
    
    storage = StateManager()
    s1 = storage.get_state("influencer-1")
    v1 = s1.version
    
    storage.commit_change("influencer-1", expected_version=v1, new_data={})
    
    s2 = storage.get_state("influencer-1")
    assert s2.version > v1
