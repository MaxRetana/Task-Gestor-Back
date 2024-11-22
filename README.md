# Django REST Framework API

This is a backend project built with Django and Django REST Framework to create a RESTful API. The application manages a `User` model with basic fields for user authentication and management.

## Features

- **Authentication**: Basic authentication system with user roles.
- **API Endpoints**: Create, read, update, and delete users.
- **Database**: PostgreSQL used as the database.
- **Environment Configuration**: `.env` file for environment variables.

## Requirements

Ensure you have the following installed:

- Python 3.8+
- PostgreSQL
- Django 4.0+
- Django REST Framework 3.12+
- pip (for Python package management)

## Models
1. Users
   - Username
   - Email
   - Password
   - Role
   - Create_at
   - Updated_at

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

## .env
  ```bash
  DATABASE_NAME=your_database_name
  DATABASE_USER=your_database_username
  DATABASE_PASSWORD=your_database_password
  DATABASE_HOST=your_database_host
  DATABASE_PORT=your_database_port
