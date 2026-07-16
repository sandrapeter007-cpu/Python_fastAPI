from fastapi import FastAPI
from pydantic import BaseModel
from models import Event, Booking
from routers import events, bookings



app = FastAPI()
app.include_router(events.router)
app.include_router(bookings.router)



# Test endpoint
@app.get("/")
def home():
    return {"message": "Event Booking API is running"}







