import uuid
from app.models import Post, PostTable
from commons.event_store import EventStore
from app.events import PostWasCreated


def test_create_posts():
    EventStore.reset_store()
    stream_id = uuid.uuid4()

    event = PostWasCreated(
        title="FooBar", 
        content="Lorem Ipsum"
    )
    EventStore.append(stream_id, event)

    post = Post.objects.latest()
    assert post.title == event.title  
    assert post.content == event.content


    