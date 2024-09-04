
import uuid
from pytest import fixture
from app.commands import CreatePostCommand, CreatePostPayload, PublishPostCommand
from commons.event_store import EventStore

@fixture 
def event_store():
    EventStore.reset_store()
    return EventStore

@fixture
def post():
    stream_id = uuid.uuid4()
    data = CreatePostPayload(stream_id, title="Test Post", content="This is a test post")
    EventStore.reset_store()

    command = CreatePostCommand(data)
    command.handle()

    return stream_id

@fixture
def published_post(post):
    command = PublishPostCommand(stream_id=post)
    command.handle()

    return post