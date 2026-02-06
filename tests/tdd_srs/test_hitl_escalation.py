import pytest

def test_low_confidence_routes_to_hitl():
    """
    SRS NFR 1.1 Requirement: Automated Escalation Logic.
    Verifies that a confidence_score below 0.70 routes content to the HITL queue.
    """
    from chimera.orchestrator import Orchestrator
    from chimera.models import TaskResult
    
    orch = Orchestrator()
    
    # Simulate a Worker result with low confidence
    result = TaskResult(
        task_id="task-123",
        content="Hello world",
        confidence_score=0.65  # Threshold is 0.70
    )
    
    routing = orch.process_result(result)
    
    assert routing.destination == "HITL_QUEUE"
    assert routing.status == "PENDING_REVIEW"

def test_sensitive_topic_mandatory_hitl():
    """
    SRS NFR 1.2 Requirement: Sensitive Topic Mandatory HITL.
    Verifies that political content ALWAYS routes to HITL, regardless of confidence.
    """
    from chimera.orchestrator import Orchestrator
    from chimera.models import TaskResult
    
    orch = Orchestrator()
    
    result = TaskResult(
        task_id="task-456",
        content="The upcoming election candidates are...",
        confidence_score=0.99,  # High confidence
        detected_topics=["politics"]
    )
    
    routing = orch.process_result(result)
    
    # Should still go to HITL because of the topic
    assert routing.destination == "HITL_QUEUE"
    assert "Sensitive topic: politics" in routing.reason
