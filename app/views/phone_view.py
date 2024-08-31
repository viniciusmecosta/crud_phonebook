from fastapi import APIRouter, HTTPException
from app.controllers.phone_controller import PhoneController
from app.observers.phone_observer import PhoneObserver

router = APIRouter()

phone_controller = PhoneController()
phone_observer = PhoneObserver()

@router.post("/phones/")
def create_phone(name: str, number: str):
    phone = phone_controller.create_phone(name, number)
    phone_observer.notify("created", phone)
    return phone

@router.get("/phones/")
def list_phones():
    return phone_controller.list_phones()

@router.put("/phones/{phone_id}")
def update_phone(phone_id: int, name: str, number: str):
    phone = phone_controller.update_phone(phone_id, name, number)
    if phone is None:
        raise HTTPException(status_code=404, detail="Phone not found")
    phone_observer.notify("updated", phone)
    return phone

@router.delete("/phones/{phone_id}")
def delete_phone(phone_id: int):
    phone = phone_controller.delete_phone(phone_id)
    if phone is None:
        raise HTTPException(status_code=404, detail="Phone not found")
    phone_observer.notify("deleted", phone)
    return phone
