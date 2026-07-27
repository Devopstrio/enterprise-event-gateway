from pkg.cloudevents.spec_v1 import CloudEventsValidator
from pkg.routing.event_router import ContentEventRouter
from pkg.deadletter.dlq_manager import DeadLetterQueueManager

def test_routing_matched():
    payload = {
        "source": "com.devopstrio.payment",
        "type": "com.devopstrio.payment.completed",
        "data": {"amount": 500}
    }
    event = CloudEventsValidator.validate_envelope(payload)
    router = ContentEventRouter()
    res = router.route_event(event)
    assert res["routed"] is True
    assert "kafka://payments-topic" in res["matched_sinks"]

def test_routing_dlq_fallback():
    payload = {
        "source": "com.devopstrio.unmatched",
        "type": "com.unknown.type",
        "data": {}
    }
    event = CloudEventsValidator.validate_envelope(payload)
    router = ContentEventRouter()
    res = router.route_event(event)
    assert res["routed"] is False
    assert "dlq://dead-letter-queue" in res["matched_sinks"]
