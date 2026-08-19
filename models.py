from pydantic import BaseModel, Field

class Event(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    availableTickets: int = Field(..., ge=0)
    eventDate: str
    eventTime: str       
    location: str
    price: float         

class Booking(BaseModel):
    userId: int
    eventId: int
    ticketCount: int = Field(..., ge=1)  


    