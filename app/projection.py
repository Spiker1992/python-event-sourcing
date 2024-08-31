from app.events import PostWasCreated
from app.models import Post


def create_post(event: PostWasCreated) -> None:
   post = Post()
   post.title = event.title
   post.content = event.content
   post.save()