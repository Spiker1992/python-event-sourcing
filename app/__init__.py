from app.events import PostWasCreated
from app.projection import create_post
from commons.event_bus import EventBus

EventBus.subscribe(PostWasCreated, create_post)