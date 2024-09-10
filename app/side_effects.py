import logging
from commons.event_listeners import SideEffect

LOGGER = logging.getLogger(__name__)

class ConfirmPostWasPublishedEmail(SideEffect):
    def handle(stream_id, event):
        LOGGER.debug('Email was sent')