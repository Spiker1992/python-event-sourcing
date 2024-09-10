from app.events import PostWasCreated, PostWasPublished
from app.projection import CreatePost, PublishPost
from app.side_effects import ConfirmPostWasPublishedEmail
from commons.event_bus import EventBus

EventBus.subscribe(PostWasCreated, CreatePost)
EventBus.subscribe(PostWasPublished, PublishPost)
EventBus.subscribe(PostWasPublished, ConfirmPostWasPublishedEmail)