import uuid
from commons.event_store import EventStore
from events import PostWasCreated


def test_persist_event():
    stream_id = uuid.uuid4()
    event = PostWasCreated(
        title="FooBar", 
        content="Lorem Ipsum"
    )
    EventStore.reset_store()

    EventStore.append(stream_id, event)

    assert EventStore.events == { stream_id: [event] }
