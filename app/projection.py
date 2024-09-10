from app.events import PostWasCreated
from app.models import Post
from commons.event_listeners import Projection
 

class CreatePost(Projection):
   def handle(steam_id, event: PostWasCreated) -> None:
      post = Post(steam_id)
      post.title = event.title
      post.content = event.content
      post.save()

class PublishPost(Projection): 
   def handle(stream_id, event) -> None: 
      post = Post.objects.get(stream_id)
      post.published = True 
      post.save()