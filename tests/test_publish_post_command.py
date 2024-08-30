
from collections import defaultdict
import uuid

from pytest import fixture
import pytest
from commands import CreatePostCommand, CreatePostPayload, PublishPostCommand
from commons.event_store import EventStore
from events import PostWasPublished

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

def test_publish_post_command(post):
    command = PublishPostCommand(stream_id=post)
    command.handle()

    event_stream = EventStore.events.get(post, [])

    assert len(event_stream) == 2
    assert event_stream[1] == PostWasPublished()

def test_cannot_publish_post_twice(published_post):
    command = PublishPostCommand(stream_id=published_post)

    with pytest.raises(Exception, match="Post is already published"):
        command.handle()
    
    event_stream = EventStore.events.get(published_post, [])

    assert len(event_stream) == 2

def test_publish_post_that_doesnt_exist():
    EventStore.reset_store()
    
    command = PublishPostCommand(stream_id=uuid.uuid4())  

    with pytest.raises(Exception, match="Post does not exist"):
        command.handle()
 
    assert EventStore.events == defaultdict(list)