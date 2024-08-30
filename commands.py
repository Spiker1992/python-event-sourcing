from dataclasses import dataclass
import uuid

from commons.event_store import EventStore
from events import PostWasCreated, PostWasPublished


@dataclass
class CreatePostPayload:
    stream_id: uuid.UUID
    title: str
    content: str

class CreatePostCommand:
    def __init__(self, data: CreatePostPayload):
        self.data = data

    def handle(self) -> None:
        event = PostWasCreated(
            title=self.data.title, 
            content=self.data.content
        )

        EventStore.append(self.data.stream_id, event)

class PublishPostCommand:
    def __init__(self, stream_id: uuid.UUID):
        self.stream_id = stream_id

    def handle(self) -> None:  
        if not self.post_exists():
            raise Exception("Post does not exist")
        
        if self.post_is_published():
            raise Exception("Post is already published")

        event = PostWasPublished()

        EventStore.append(self.stream_id, event)

    def post_exists(self):
        return EventStore.events.get(self.stream_id, None) is not None

    def post_is_published(self):
        for event in EventStore.events.get(self.stream_id, []):
            if isinstance(event, PostWasPublished):
                return True
            
        return  False