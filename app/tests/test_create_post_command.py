
import uuid
from app.commands import CreatePostCommand, CreatePostPayload
from app.events import PostWasCreated


def test_create_post_command(event_store):
    stream_id = uuid.uuid4()
    data = CreatePostPayload(stream_id, title="Test Post", content="This is a test post")

    command = CreatePostCommand(data)
    command.handle()

    expected_event = PostWasCreated(
        title=data.title, 
        content=data.content
    )

    assert event_store.events == { stream_id: [expected_event]}
    