# Hotel Booking API

A Django REST API for hotel property listings and reservation management with multi-language support.

## Features
- Property listings with images, GPS coordinates, pricing
- Reservation system with date-range booking
- Newsletter subscription and customer inquiry system
- Trilingual support (EN/DE/SR)

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/properties` | List all hotels |
| GET | `/api/property/<id>/` | Hotel details |
| POST | `/api/reservation` | Book a room |
| POST | `/api/newsletter` | Subscribe |
| POST | `/api/customer_message` | Send inquiry |
