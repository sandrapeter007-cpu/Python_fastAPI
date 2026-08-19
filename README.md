# Event Booking API

## Description
A RESTful Event Booking API built with FastAPI and Python. It allows users to view events, book tickets, and lets owners manage events. The API handles validation and error cases such as overbooking or accessing a deleted event.

---

## Tech Stack
- Python 3.x
- FastAPI
- Pydantic
- Uvicorn

---

## How to Run the Service

### 1. Clone the repository
```bash
git clone https://github.com/sandrapeter007-cpu/cloud-accelerator-program.git
cd cloud-accelerator-program
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the application
```bash
uvicorn main:app --reload
```

API runs at: `http://127.0.0.1:8000`  
Swagger docs: `http://127.0.0.1:8000/docs`

---

## Endpoints

### User
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /events | See all available events |
| GET | /events/{event_id} | Get a specific event by ID |
| POST | /bookings | Book tickets for an event |
| GET | /users/{user_id}/bookings | See all bookings for a user |

### Owner
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /events | Add a new event |
| DELETE | /events/{event_id} | Delete an event |
| GET | /events/{event_id}/bookings | See booked tickets for an event |

---

## Example Requests

### Create an Event
**POST** `/events`
```json
{
  "id": 1,
  "name": "Music Concert",
  "eventDate": "2026-08-10",
  "eventTime": "18:00",
  "location": "Berlin",
  "availableTickets": 100,
  "price": 29.99
}
```

### Get All Events
**GET** `/events`

### Get a Single Event
**GET** `/events/1`

### Book Tickets
**POST** `/bookings`
```json
{
  "userId": 1,
  "eventId": 1,
  "ticketCount": 2
}
```

### Get User Bookings
**GET** `/users/1/bookings`

### Get Event Bookings (Owner)
**GET** `/events/1/bookings`

### Delete Event (Owner)
**DELETE** `/events/1`

---

## Assumptions
- Data is stored in memory — no database is used. Data resets on server restart.
- User identity is passed as a plain `userId` — no authentication is implemented.
- A booking cannot exceed the number of available tickets.
- Deleting an event also deletes all associated bookings.
- Event IDs are provided by the caller and must be unique.
- TODO: Consider soft-deleting events to preserve user booking history.