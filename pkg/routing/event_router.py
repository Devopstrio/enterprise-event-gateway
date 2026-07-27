from typing import Dict, Any, List
from pkg.cloudevents.spec_v1 import CloudEventV1

class ContentEventRouter:
    """
    Content-Based Event Routing Matrix & Filter Evaluator.
    Evaluates event type and payload fields to determine destination sinks (e.g. SQS, Kafka, Webhook).
    """

    def __init__(self):
        self.routing_rules = [
            {"type_prefix": "com.devopstrio.payment.", "target_sink": "kafka://payments-topic"},
            {"type_prefix": "com.devopstrio.user.", "target_sink": "sqs://user-events-queue"},
            {"type_prefix": "com.devopstrio.audit.", "target_sink": "s3://audit-logs-bucket"}
        ]

    def route_event(self, event: CloudEventV1) -> Dict[str, Any]:
        matched_sinks = []
        for rule in self.routing_rules:
            if event.type.startswith(rule["type_prefix"]):
                matched_sinks.append(rule["target_sink"])

        if not matched_sinks:
            matched_sinks.append("dlq://dead-letter-queue")

        return {
            "event_id": event.id,
            "event_type": event.type,
            "matched_sinks": matched_sinks,
            "routed": True if "dlq://" not in matched_sinks[0] else False
        }
