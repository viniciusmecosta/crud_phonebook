from controllers.phonebook_controller import PhonebookController
from models.phonebook import Phonebook

class PhonebookObserver:
    def __init__(self, controller: PhonebookController):
        self.controller = controller

    def handle_event(self, event: str, data: any):
        print(f"Received event '{event}' with data: {data}")

    def notify(self, event: str, data: any):
        self.handle_event(event, data)

    def on_create(self, phonebook_entry: Phonebook):
        self.notify("create", phonebook_entry)

    def on_update(self, id: int, phonebook_entry: Phonebook):
        self.notify("update", phonebook_entry)

    def on_delete(self, id: int):
        self.notify("delete", id)