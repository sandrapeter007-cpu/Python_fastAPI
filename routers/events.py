from fastapi import APIRouter, HTTPException
from models import Event
from storage import events
import storage

router = APIRouter()


@router.get("/events")
def get_events():
    if not events:
        return {"message": "No events available"}
    return events



@router.post("/events")
def create_event(event: Event):
    for existing_event in events:
        if existing_event.id == event.id:
            raise HTTPException(status_code=400, detail="Event ID already exists")
    events.append(event)
    return event

@router.get("/events/{event_id}")
def get_event(event_id: int):
    for event in storage.events:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")


@router.delete("/events/{event_id}")
def delete_event(event_id: int):
    for event in storage.events:
        if event.id == event_id:
            storage.events.remove(event)
            storage.bookings[:] = [
                booking for booking in storage.bookings
                if booking.eventId != event_id 
            ]
            return {"message": "Event deleted successfully"}

    raise HTTPException(status_code=404, detail="Event not found")