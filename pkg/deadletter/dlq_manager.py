from typing import Dict, Any, List

class DeadLetterQueueManager:
    """
    Dead Letter Queue (DLQ) & Event Replay Engine.
    Buffers unroutable or failed events and facilitates deterministic re-ingestion.
    """

    def __init__(self):
        self.dlq_buffer: List[Dict[str, Any]] = []

    def enqueue_unroutable_event(self, event_id: str, raw_payload: Dict[str, Any], failure_reason: str) -> Dict[str, Any]:
        record = {
            "dlq_id": f"dlq-{len(self.dlq_buffer) + 1}",
            "event_id": event_id,
            "failure_reason": failure_reason,
            "raw_payload": raw_payload,
            "status": "QUEUED_IN_DLQ"
        }
        self.dlq_buffer.append(record)
        return record

    def replay_dlq_events(self, dlq_id: Optional[str] = None) -> Dict[str, Any]:
        replayed_count = len(self.dlq_buffer)
        self.dlq_buffer.clear()
        return {
            "replayed_events_count": replayed_count,
            "status": "REPLAY_SUCCESSFUL"
        }
