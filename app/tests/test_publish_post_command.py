
from collections import defaultdict
import uuid

import pytest
from app.commands import PublishPostCommand
from app.events import PostWasPublished


def test_publish_post_command(event_store, post):
    command = PublishPostCommand(stream_id=post)
    command.handle()

    event_stream = event_store.events.get(post, [])

    assert len(event_stream) == 2
    assert event_stream[1] == PostWasPublished()

def test_cannot_publish_post_twice(event_store, published_post):
    command = PublishPostCommand(stream_id=published_post)

    with pytest.raises(Exception, match="Post is already published"):
        command.handle()
    
    event_stream = event_store.events.get(published_post, [])

    assert len(event_stream) == 2

def test_publish_post_that_doesnt_exist(event_store):
    command = PublishPostCommand(stream_id=uuid.uuid4())  

    with pytest.raises(Exception, match="Post does not exist"):
        command.handle()
 
    assert event_store.events == defaultdict(list)