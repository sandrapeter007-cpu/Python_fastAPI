# Event Booking API

## Description

This is a RESTful Event Booking API built using FastAPI and Python. It allows users to create and manage events, book tickets for events, and retrieve booking information. The API performs input validation and handles common error scenarios such as booking more tickets than available or booking for a deleted event.

---

## Features

- Create an event
- Get all events
- Get an event by ID
- Update an event
- Delete an event
- Book tickets for an event
- Get all bookings for a user
- Get all bookings for an event

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
git clone https://github.com/sandrapeterv07-cpu/cloud-accelerator-program.git
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

The API will run at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Example Requests

### Create an Event

**POST** `/events`

Example request body:

```json
{
  "name": "Music Concert",
  "date": "2026-08-10",
  "location": "Berlin",
  "total_tickets": 100
}
```

---

### Get All Events

**GET**

```
/events
```

---

### Book Tickets

**POST**

```
/bookings
```

Example request body:

```json
{
  "user_id": 1,
  "event_id": 1,
  "tickets": 2
}
```

---

### Get User Bookings

**GET**

```
/bookings/user/1
```

---

### Get Event Bookings

**GET**

```
/bookings/event/1
```

---

## Assumptions

- Data is stored in memory (no database is used).
- Event IDs and Booking IDs are generated automatically.
- A booking cannot exceed the number of available tickets.
- Deleting an event removes the event from the event list. Associated booking behavior depends on the implemented logic.
- Input validation is handled using Pydantic models.