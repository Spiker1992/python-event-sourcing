from app.events import PostWasCreated
from app.projection import CreatePost
from commons.event_bus import EventBus

EventBus.subscribe(PostWasCreated, CreatePost)