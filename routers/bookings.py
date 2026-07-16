from fastapi import APIRouter, HTTPException
from models import Booking
from storage import bookings, events

router = APIRouter()


@router.post("/bookings")
def book_ticket(booking: Booking):

    for event in events:
        if event.id == booking.eventId:

            if event.availableTickets > 0:
                event.availableTickets -= 1
                bookings.append(booking)

                return {
                    "message": "Ticket booked successfully"
                }

            raise HTTPException(
                status_code=400,
                detail="No tickets available"
            )

    raise HTTPException(
        status_code=404,
        detail="Event not found"
    )


@router.get("/users/{user_id}/bookings")
def get_user_bookings(user_id: int):

    user_bookings = []

    for booking in bookings:
        if booking.userId == user_id:
            user_bookings.append(booking)

    return user_bookings


@router.get("/events/{event_id}/bookings")
def get_event_bookings(event_id: int):

    count = 0

    for booking in bookings:
        if booking.eventId == event_id:
            count += 1

    return {
        "eventId": event_id,
        "bookedTickets": count
    }