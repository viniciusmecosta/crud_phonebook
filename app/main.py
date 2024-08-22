from fastapi import FastAPI
from controllers.phonebook_controller import PhonebookController
from observers.phonebook_observer import PhonebookObserver

app = FastAPI()

controller = PhonebookController()
observer = PhonebookObserver(controller)

@app.on_event("startup")
async def startup_event():
    controller.observer = observer