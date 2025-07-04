# Expense Tracker API

This is a RESTful API for tracking personal expenses and income, built with Django and Django REST Framework. It features JWT-based authentication, role-based access control, automatic tax calculations, and complete CRUD functionality.

## Key Features

*   **Secure Authentication**: User registration and login system using JSON Web Tokens (JWT).
*   **Role-Based Access**:
    *   **Regular Users**: Can only create, view, update, and delete their own financial records.
    *   **Superusers**: Have administrative access to view and manage all records in the system.
*   **CRUD Operations**: Full Create, Read, Update, and Delete functionality for expense and income records.
*   **Automatic Tax Calculation**: Supports both `flat` and `percentage` tax calculations on records.
*   **Pagination**: List endpoints are paginated for efficient data handling.
*   **Comprehensive Test Suite**: Includes a full suite of automated tests to ensure API reliability.

## Technical Stack

*   **Backend**: Python, Django
*   **API**: Django REST Framework
*   **Authentication**: djangorestframework-simplejwt
*   **Database**: SQLite (for development)

---

## Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the Repository**
```bash
git clone <your-repository-url>
cd virth
```

**2. Create and Activate a Virtual Environment**
```bash
# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

**3. Install Dependencies**
```bash
pip install django djangorestframework djangorestframework-simplejwt
```

**4. Apply Database Migrations**
This command creates the necessary database tables based on the models.
```bash
python manage.py migrate
```

**5. Create a Superuser**
This creates an administrative user who can access all records.
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

**6. Run the Development Server**
```bash
python manage.py runserver
```
The API will now be available at `http://127.0.0.1:8000/`.

---

## API Endpoints Documentation

All requests to protected endpoints must include an `Authorization` header with a valid JWT token: `Authorization: Bearer <your_access_token>`.

### Authentication

| Method | Endpoint              | Description                                |
| :----- | :-------------------- | :----------------------------------------- |
| `POST` | `/api/auth/register/` | Creates a new user account.                |
| `POST` | `/api/auth/login/`    | Authenticates a user and returns JWT tokens. |
| `POST` | `/api/auth/refresh/`  | Generates a new access token.              |

**Example: Login Request Body**
```json
{
    "username": "your-username",
    "password": "your-password"
}
```

### Expense & Income Records

| Method   | Endpoint            | Auth      | Description                                     |
| :------- | :------------------ | :-------- | :---------------------------------------------- |
| `POST`   | `/api/expenses/`    | Required  | Creates a new expense or income record.         |
| `GET`    | `/api/expenses/`    | Required  | Lists all records for the authenticated user.   |
| `GET`    | `/api/expenses/{id}/` | Required  | Retrieves a single record by its ID.            |
| `PUT`    | `/api/expenses/{id}/` | Required  | Updates an existing record.                     |
| `DELETE` | `/api/expenses/{id}/` | Required  | Deletes a record.                               |

**Example: Create Record (`POST /api/expenses/`)**

*Request Body:*
```json
{
    "title": "Web Development Project",
    "description": "Freelance work for client X",
    "amount": "2500.00",
    "transaction_type": "credit",
    "tax": "15",
    "tax_type": "percentage"
}
```

*Success Response (201 Created):*
```json
{
    "id": 1,
    "title": "Web Development Project",
    "description": "Freelance work for client X",
    "amount": "2500.00",
    "transaction_type": "credit",
    "tax": "15.00",
    "tax_type": "percentage",
    "total": "2875.00",
    "created_at": "2025-07-04T10:00:00Z",
    "updated_at": "2025-07-04T10:00:00Z"
}
```

## Postman Collection

A Postman collection is available in the root directory: `Expence_tracker.postman_collection.json`. You can import this into Postman to easily test all API endpoints.
