from fastapi import APIRouter
from models.phonebook import Phonebook

router = APIRouter()

class PhonebookController:
    def __init__(self):
        self.phonebook = []

    def create_phonebook_entry(self, phonebook_entry: Phonebook):
        self.phonebook.append(phonebook_entry)
        return phonebook_entry

    def get_phonebook_entries(self):
        return self.phonebook

    def update_phonebook_entry(self, id: int, phonebook_entry: Phonebook):
        for entry in self.phonebook:
            if entry.id == id:
                entry.name = phonebook_entry.name
                entry.phone_number = phonebook_entry.phone_number
                return entry
        return None

    def delete_phonebook_entry(self, id: int):
        for entry in self.phonebook:
            if entry.id == id:
                self.phonebook.remove(entry)
                return True
        return False