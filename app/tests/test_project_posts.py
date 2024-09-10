import uuid
from app.models import Post
from app.events import PostWasCreated, PostWasPublished


def test_create_posts(event_store):  
    stream_id = uuid.uuid4()

    event = PostWasCreated(
        title="FooBar", 
        content="Lorem Ipsum"
    )
    event_store.append(stream_id, event)

    post = Post.objects.latest()
    assert post.title == event.title  
    assert post.content == event.content

def test_publish_posts(event_store):  
    stream_id = uuid.uuid4()

    (Post(stream_id)).save()

    event = PostWasPublished()
    event_store.append(stream_id, event)

    post = Post.objects.get(stream_id)
    assert post.published is True
    