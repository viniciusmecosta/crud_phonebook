class PhoneObserver:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, func):
        self.subscribers.append(func)

    def unsubscribe(self, func):
        self.subscribers.remove(func)

    def notify(self, event_type: str, phone):
        for subscriber in self.subscribers:
            subscriber(event_type, phone)
