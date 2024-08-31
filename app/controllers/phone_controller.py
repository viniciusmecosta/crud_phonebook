from typing import List, Optional
from app.models.phone_model import Phone

class PhoneController:
    def __init__(self):
        self.phones = []
        self.current_id = 1

    def create_phone(self, name: str, number: str) -> Phone:
        phone = Phone(id=self.current_id, name=name, number=number)
        self.phones.append(phone)
        self.current_id += 1
        return phone

    def list_phones(self) -> List[Phone]:
        return self.phones

    def update_phone(self, phone_id: int, name: str, number: str) -> Optional[Phone]:
        for phone in self.phones:
            if phone.id == phone_id:
                phone.name = name
                phone.number = number
                return phone
        return None

    def delete_phone(self, phone_id: int) -> Optional[Phone]:
        for phone in self.phones:
            if phone.id == phone_id:
                self.phones.remove(phone)
                return phone
        return None
