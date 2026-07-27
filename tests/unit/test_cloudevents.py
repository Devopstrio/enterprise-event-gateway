from pkg.cloudevents.spec_v1 import CloudEventsValidator, CloudEventV1

def test_cloudevents_valid_envelope():
    payload = {
        "specversion": "1.0",
        "source": "com.devopstrio.test",
        "type": "com.devopstrio.test.event",
        "data": {"status": "OK"}
    }
    event = CloudEventsValidator.validate_envelope(payload)
    assert isinstance(event, CloudEventV1)
    assert event.specversion == "1.0"
    assert event.source == "com.devopstrio.test"
