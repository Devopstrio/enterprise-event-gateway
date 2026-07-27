import sys
import json
from pkg.cloudevents.spec_v1 import CloudEventsValidator
from pkg.routing.event_router import ContentEventRouter
from pkg.deadletter.dlq_manager import DeadLetterQueueManager

def main():
    """
    eegctl - Enterprise Event Gateway CLI Utility.
    Usage: python -m cmd.eegctl.main <command>
    Commands: validate, route, replay
    """
    if len(sys.argv) < 2:
        print("eegctl CLI - Usage: python -m cmd.eegctl.main [validate|route|replay]")
        sys.exit(0)

    cmd = sys.argv[1]
    validator = CloudEventsValidator()
    router = ContentEventRouter()
    dlq = DeadLetterQueueManager()

    if cmd == "validate":
        sample = {
            "specversion": "1.0",
            "source": "com.devopstrio.payment",
            "type": "com.devopstrio.payment.completed",
            "data": {"amount": 100}
        }
        event = validator.validate_envelope(sample)
        print(f"Validated CloudEvent ID: {event.id}")
    elif cmd == "route":
        sample = {
            "specversion": "1.0",
            "source": "com.devopstrio.payment",
            "type": "com.devopstrio.payment.completed",
            "data": {"amount": 100}
        }
        event = validator.validate_envelope(sample)
        res = router.route_event(event)
        print(f"Routed Event {res['event_id']} -> {res['matched_sinks']}")
    elif cmd == "replay":
        res = dlq.replay_dlq_events()
        print(f"DLQ Replay Status: {res['status']}")
    else:
        print(f"Unknown command '{cmd}'")

if __name__ == "__main__":
    main()
