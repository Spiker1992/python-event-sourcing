from collections import defaultdict

class EventBus:
    _listeners = defaultdict(list)

    @classmethod
    def subscribe(cls, event_type, listener):
        cls._listeners[event_type].append(listener)

    @classmethod
    def publish(cls, stream_id, event):
        for listener in cls._listeners[type(event)]:
            (listener).handle(stream_id, event)
