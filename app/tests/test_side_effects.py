import uuid
import logging
from app.events import PostWasPublished
from app.side_effects import ConfirmPostWasPublishedEmail
from commons.event_bus import EventBus

LOGGER = logging.getLogger(__name__)

def test_confirmation_email_is_sent_on_post_publish(event_store, caplog):  
    caplog.set_level(logging.DEBUG)

    stream_id = uuid.uuid4()
    EventBus._listeners[PostWasPublished] = [ConfirmPostWasPublishedEmail]

    event = PostWasPublished()
    event_store.append(stream_id, event)

    assert 'Email was sent' in caplog.text
