import uuid
from collections import defaultdict

from commons.event_bus import EventBus


class EventStore:
    events = defaultdict(list)

    @classmethod
    def append(cls, stream_id: uuid.UUID, event) -> None:
        cls.events[stream_id].append(event)

        EventBus.publish(event)

    @classmethod
    def reset_store(cls) -> None:
        cls.events = defaultdict(list)