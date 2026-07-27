import uuid
from datetime import datetime, timezone
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class CloudEventV1(BaseModel):
    """
    CNCF CloudEvents v1.0 Specification Implementation.
    """
    specversion: str = Field("1.0", description="CloudEvents specification version")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Event unique identifier")
    source: str = Field(..., description="URI identifying the event producer context")
    type: str = Field(..., description="Domain-specific event type identifier")
    datacontenttype: str = Field("application/json", description="Content type of event data")
    time: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat(), description="Timestamp of event occurrence")
    data: Dict[str, Any] = Field(default_factory=dict, description="Event payload data")

class CloudEventsValidator:
    """
    Validates incoming payloads against CloudEvents v1.0 format.
    """
    @staticmethod
    def validate_envelope(payload: Dict[str, Any]) -> CloudEventV1:
        return CloudEventV1(**payload)
