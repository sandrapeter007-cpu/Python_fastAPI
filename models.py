from pydantic import BaseModel, Field
from datetime import date

# Event data structure
class Event(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    availableTickets: int = Field(..., ge=0)
    eventDate: str
    location: str

class Booking(BaseModel):
    userId: int
    eventId: int
