import uuid
from commons.event_store import EventStore
from dataclasses import dataclass


@dataclass
class DummyEvent():
    title: str
    content: str

def test_persist_event():
    stream_id = uuid.uuid4()
    event = DummyEvent(
        title="FooBar", 
        content="Lorem Ipsum"
    )
    EventStore.reset_store()

    EventStore.append(stream_id, event)

    assert EventStore.events == { stream_id: [event] }
