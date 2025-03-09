# MyProject

MyProject is a Django-based application designed for user registration and management, following Clean Architecture principles. This project aims to demonstrate best practices in software design, including separation of concerns, maintainability, and testability.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration with secure password hashing
- User retrieval by username
- RESTful API endpoints for user management
- Unit tests covering all layers of the application
- Clear separation of concerns following Clean Architecture

## Technologies Used

- **Python**: Programming language used for backend development.
- **Django**: Web framework for building the application.
- **Django REST Framework**: Toolkit for building Web APIs.
- **SQLite**: Lightweight database for development (can be replaced with PostgreSQL or other databases in production).
- **pytest**: Framework for writing and running tests.

## Architecture

The application follows the Clean Architecture principles, which emphasize a clear separation of concerns and independence of frameworks. The project's structure includes:

- **Domain Layer**: Contains business logic and data models.
- **Service Layer**: Encapsulates business rules and operations.
- **Repository Layer**: Manages data access and storage.
- **API Layer**: Handles HTTP requests and responses.

### Diagram

```
+-------------------+
|    API Layer      |
| (Views, Serializers)|
+-------------------+
          |
+-------------------+
|  Service Layer    |
| (Business Logic)  |
+-------------------+
          |
+-------------------+
| Repository Layer   |
| (Data Access)     |
+-------------------+
          |
+-------------------+
|    Domain Layer    |
| (Models)          |
+-------------------+
```

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/myproject.git
   cd myproject
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   The server will start at `http://127.0.0.1:8000/`.

### Configuration

You may want to configure environment variables for production, such as database settings, secret keys, and debug options. Create a `.env` file or use any preferred method for managing environment variables.

## Usage

### API Endpoints

- **Register a User**: `POST /api/users/`
  - **Request Body**:
    ```json
    {
      "username": "newuser",
      "email": "newuser@example.com",
      "password": "password123"
    }
    ```
  - **Response**: 201 Created with user details.

- **Get User by Username**: `GET /api/users/{username}/`
  - **Response**: 
    - 200 OK (User details)
    - 404 Not Found (if user does not exist)

### Example Usage

1. **Register a user**:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/users/ -H "Content-Type: application/json" -d '{"username": "newuser", "email": "newuser@example.com", "password": "password123"}'
   ```

2. **Retrieve a user**:
   ```bash
   curl -X GET http://127.0.0.1:8000/api/users/newuser/
   ```

## Running Tests

To ensure the integrity of the application, run the tests with:

```bash
python manage.py test users/tests/
```

This will execute all unit tests for the application, covering the domain, repository, service, and API layers.

## Project Structure

```
djangoCleanArch/
│
├── users/
│   ├── api/
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── domain/
│   │   └── models.py
│   ├── management/
│   │   ├── commands
│   │       ├── seed_users.py
│   ├── repositories/
│   │   └── user_repository.py
│   ├── services/
│   │   └── user_service.py
│   └── tests/
│       ├── test_api.py
│       ├── test_domain.py
│       ├── test_repository.py
│       └── test_service.py
│
├── myproject/
│   ├── config
│       ├── urls.py
│       ├── settings.py
│       └── wsgi.py
│
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request. Ensure that your code adheres to the project's coding standards and that all tests pass.
