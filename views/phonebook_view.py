from fastapi import APIRouter
from controllers.phonebook_controller import PhonebookController
from models.phonebook import Phonebook 
router = APIRouter()

class PhonebookView:
    def __init__(self):
        self.controller = PhonebookController()

    @router.post("/phonebook/")
    async def create_phonebook_entry(phonebook_entry: Phonebook):
        return self.controller.create_phonebook_entry(phonebook_entry)

    @router.get("/phonebook/")
    async def get_phonebook_entries():
        return self.controller.get_phonebook_entries()

    @router.put("/phonebook/{id}")
    async def update_phonebook_entry(id: int, phonebook_entry: Phonebook):
        return self.controller.update_phonebook_entry(id, phonebook_entry)

    @router.delete("/phonebook/{id}")
    async def delete_phonebook_entry(id: int):
        return self.controller.delete_phonebook_entry(id)