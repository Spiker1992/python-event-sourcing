import uuid
from collections import defaultdict


class EventStore:
    events = defaultdict(list)

    @classmethod
    def append(cls, stream_id: uuid.UUID, event) -> None:
        cls.events[stream_id].append(event)

    @classmethod
    def reset_store(cls) -> None:
        cls.events = defaultdict(list)