# Event Booking API

A RESTful Event Booking API built with FastAPI.

## Features

- View all events
- Create a new event
- Delete an event
- Book a ticket
- View all bookings for a user
- View the number of booked tickets for an event

## Tech Stack

- Python 3
- FastAPI
- Uvicorn

## Project Structure

```
event-booking-api
│
├── main.py
├── models.py
├── storage.py
├── requirements.txt
├── README.md
│
├── routers
│   ├── events.py
│   └── bookings.py
```

## Installation

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

**macOS/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Example API Endpoints

- GET `/events`
- POST `/events`
- DELETE `/events/{event_id}`
- POST `/bookings`
- GET `/users/{user_id}/bookings`
- GET `/events/{event_id}/bookings`

## Assumptions

- No authentication is implemented.
- Users are identified by `userId`.
- Data is stored in memory and will be lost when the server restarts.

## Future Improvements

- Add a database (SQLite/PostgreSQL)
- Implement authentication and authorization
- Generate event IDs automatically
- Add unit tests