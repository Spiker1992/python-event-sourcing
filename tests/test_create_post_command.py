
import uuid
from app.commands import CreatePostCommand, CreatePostPayload
from commons.event_store import EventStore
from app.events import PostWasCreated


def test_create_post_command():
    stream_id = uuid.uuid4()
    data = CreatePostPayload(stream_id, title="Test Post", content="This is a test post")
    EventStore.reset_store()

    command = CreatePostCommand(data)
    command.handle()

    expected_event = PostWasCreated(
        title=data.title, 
        content=data.content
    )

    assert EventStore.events == { stream_id: [expected_event]}
    