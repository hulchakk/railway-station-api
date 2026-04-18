# Railway Station API

A comprehensive backend system for managing railway operations, including routes, journeys, ticketing, and user orders. Built with Django and Django REST Framework.

## Features

### Infrastructure Management
* **Stations:** CRUD operations for railway stations with geographic coordinates (latitude and longitude).
* **Routes:** Management of travel paths between source and destination stations including distance tracking.
* **Trains & Types:** Support for various train types and specific train configurations (number of cargos and places per cargo).
* **Crew:** Management of staff members (first name and last name) assigned to journeys.

### Travel & Booking
* **Journeys:** Scheduling of trips with specific routes, trains, and assigned crew members.
* **Ticketing:** Integrated seat and cargo allocation for journeys.
* **Orders:** Unified order management system that handles nested ticket creation.

### User Management
* **Authentication:** Secure access via JWT (JSON Web Tokens).
* **User Profiles:** Registration and profile management, including support for user avatars.
* **Personal Data:** Users can manage their own profile and view a personal history of orders and tickets.

### Technical Capabilities
* **Filtering:** - Journeys: search by source, destination, departure, and arrival dates.
    - Orders: search by creation timeframe (before/after).
    - Infrastructure: case-insensitive search for stations, trains, and crew by name.
* **Pagination:** All list endpoints support limit/offset pagination for performance.
* **Security:** Global permission sets combined with object-level ownership (IsOwner) for sensitive data.


## Installation

1. Clone the repository:
```bash
git clone <repository-url>