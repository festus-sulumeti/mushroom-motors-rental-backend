# Mushroom Motors Rental Backend

Mushroom Motors Rental Backend is a robust and scalable backend system for managing a vehicle rental service.  
**This project is built with Python and Flask.**  
It provides RESTful APIs for vehicle inventory, user management, booking, payments, and administrative operations. The backend is designed for reliability, security, and extensibility.

## Features

- **User Authentication & Authorization:** Secure registration, login, and role-based access control.
- **Vehicle Inventory Management:** CRUD operations for vehicles, categories, and availability.
- **Booking System:** End-to-end booking workflow, including availability checks and reservation management.
- **Payment Integration:** Support for payment gateways and transaction tracking.
- **Admin Dashboard APIs:** Administrative endpoints for reporting, analytics, and system management.
- **Automated Testing:** Comprehensive test suite for all major features.
- **Environment Configuration:** Flexible configuration for different deployment environments.

## Architecture

- **Flask Framework:** Lightweight Python web framework for building RESTful APIs.
- **MVC Pattern:** Separation of concerns using Models, Views (API responses), and Controllers.
- **Service Layer:** Business logic is encapsulated in services for maintainability.
- **Database:** Relational database (e.g., PostgreSQL/MySQL) managed via migrations.
- **Environment Variables:** Sensitive data and configuration managed via `.env` files.

## Project Structure

- **src/**  
  Main application source code:
  - `controllers/` — Handle HTTP requests and responses.
  - `models/` — Define database schemas and ORM models.
  - `routes/` — API route definitions.
  - `services/` — Business logic and integrations.
  - `utils/` — Utility functions and helpers.

- **config/**  
  Configuration files for environment variables, database connections, and third-party services.

- **migrations/**  
  Database migration scripts for schema evolution.

- **tests/**  
  Automated unit and integration tests.

- **package.json**  
  Project manifest: dependencies, scripts, and metadata.

- **.env**  
  Environment variables for secrets and configuration.  
  **Should be in `.gitignore`** to protect sensitive data.

- **.gitignore**  
  Specifies files and directories to exclude from version control.

## Files & Folders Explained

- **src/**: All backend logic and API endpoints.
- **config/**: Centralized configuration management.
- **migrations/**: Database schema changes and versioning.
- **tests/**: Ensures code reliability and correctness.
- **package.json**: Dependency and script management.
- **.env**: Secrets and environment-specific settings.
- **.gitignore**: Prevents sensitive and unnecessary files from being tracked.

## Why Certain Files Are in `.gitignore`

- **.env**: Contains secrets (API keys, passwords) that must not be exposed.
- **node_modules/**: Dependency binaries; can be restored from `package.json`.
- **logs/**: Runtime logs; may contain sensitive info and grow large.
- **coverage/**: Test coverage reports; generated during CI/testing.
- **dist/** or **build/**: Compiled output; not needed in source control.
- **tmp/**: Temporary files; not relevant for versioning.

## Getting Started

1. **Clone the repository:**  
```bash
   git clone https://github.com/festus-sulumeti/mushroom-motors-rental-backend.git

```
```bash
   cd mushroom-motors-rental-backend
```

2. **Create and activate a virtual environment:**  
```bash
   python3 -m venv venv
```
```bash
   source venv/bin/activate
```

3. **Install dependencies:**  
 ```bash
   pip install -r requirements.txt
 ```

4. **Configure environment:**  
   Copy `.env.example` to `.env` and set required variables.

5. **Run database migrations:**  

alembic
```bash
  pip install alembic
```
```bash
 alembic init alembic
```

   
 ```bash
   flask db upgrade
   # or, if using Alembic directly
   alembic upgrade head
 ```

6. **Start the server:**  
```bash
   flask run
```
   or 

```bash
   python app.py   
```

7. **Run tests:**  
```bash
   pytest
```

## Contributing

- Fork the repository and create your branch.
- Write clear, tested code and follow the style guide.
- Submit pull requests with detailed descriptions.

## License

MIT License. See `LICENSE` for details.

## Contact

For questions or support, please open an issue or contact the maintainers.

## Contact

For questions or support, please open an issue or contact the maintainers.

