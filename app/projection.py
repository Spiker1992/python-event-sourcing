from app.events import PostWasCreated
from app.models import Post
from commons.event_listeners import Projection
 

class CreatePost(Projection):
   def handle(event: PostWasCreated) -> None:
      post = Post()
      post.title = event.title
      post.content = event.content
      post.save()