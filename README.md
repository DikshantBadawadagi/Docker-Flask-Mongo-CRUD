# Flask MongoDB CRUD API

This project is a Flask-based application that provides CRUD (Create, Read, Update, Delete) operations on a MongoDB database for managing a `User` resource using a REST API.

## Project Overview

The application exposes the following REST API endpoints:

- **GET /users**: Returns a list of all users.
- **GET /users/<id>**: Returns the user with the specified ID.
- **POST /users**: Creates a new user with the provided data (name, email, and password).
- **PUT /users/<id>**: Updates an existing user with the specified ID and new data.
- **DELETE /users/<id>**: Deletes the user with the specified ID.

The application uses Flask for the web framework, MongoDB for data storage, and Docker for containerization.

## Requirements

- **Flask**: Web framework for building the API.
- **Flask-PyMongo**: Flask extension for working with MongoDB.
- **Werkzeug**: For password hashing.
- **Postman**: For testing the API.
- **Docker**: For running the application in a container.

## Features

- **User Management**: CRUD operations on a User resource with fields: id, name, email, and password.
- **Password Security**: Passwords are hashed before being stored in the database.
- **MongoDB Integration**: The app uses MongoDB as the database for storing and retrieving user data.
- **Docker Support**: The app is containerized using Docker for easy deployment and portability.
- **API Testing**: The API is tested using Postman to verify correct functionality.

## Tech Stack

- **Frontend**: None (API-based backend).
- **Backend**: Flask (Python web framework).
- **Database**: MongoDB.
- **Containerization**: Docker.
- **Libraries**: Flask, Flask-PyMongo, Werkzeug, and more.

## Setup and Installation

### Prerequisites

Before running the application, ensure you have the following installed:

- **Docker**: Install Docker to run the application in a container.
- **Postman**: For testing the API endpoints.

### Steps to Set Up

1. **Clone the Repository**

   ```bash
   git clone https://github.com/DikshantBadawadagi/Docker-Flask-Mongo-CRUD
## Build and Run the Docker Container

You can use Docker to run the Flask application and MongoDB in containers. First, make sure Docker is running, then:

```bash
docker-compose up --build
This will start the application and MongoDB in separate containers. The Flask app will be accessible at http://127.0.0.1:5000.

Environment Variables
Ensure you have the following environment variables set in the .env file:

SECRET_KEY: A secret key for Flask (can be generated using Python).
MONGO_URI: The connection string for MongoDB (e.g., mongodb://mongo:27017/flask_mongodb_crud).
Run the Application
Once the containers are up and running, you can access the API at http://127.0.0.1:5000.

Running Locally (Without Docker)
To run the app without Docker, install the dependencies and run the app directly:

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
Open the app in your browser: http://127.0.0.1:5000.

API Endpoints
GET /users: Retrieve all users.
Request:

bash
Copy code
GET http://127.0.0.1:5000/users
Response:

json
Copy code
[
  {
    "id": "1",
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
]
GET /users/<id>: Retrieve a user by their ID.
Request:

bash
Copy code
GET http://127.0.0.1:5000/users/{id}
Response:

json
Copy code
{
  "id": "1",
  "name": "John Doe",
  "email": "johndoe@example.com"
}
POST /users: Create a new user.
Request:

bash
Copy code
POST http://127.0.0.1:5000/users
Body:

json
Copy code
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "password": "securepassword"
}
Response:

json
Copy code
{
  "id": "12345"
}
PUT /users/<id>: Update an existing user.
Request:

bash
Copy code
PUT http://127.0.0.1:5000/users/{id}
Body:

json
Copy code
{
  "name": "John Doe Updated",
  "email": "newemail@example.com",
  "password": "newpassword"
}
Response:

json
Copy code
{
  "message": "User updated successfully."
}
DELETE /users/<id>: Delete a user.
Request:

bash
Copy code
DELETE http://127.0.0.1:5000/users/{id}
Response:

json
Copy code
{
  "message": "User deleted successfully."
}
Testing the API
To test the API endpoints:

Open Postman.
Create a new HTTP request for each endpoint.
Send requests and check the responses to verify CRUD functionality.
Example Postman Setup:
GET /users: List all users.
POST /users: Create a user by providing the necessary data (name, email, password).
PUT /users/{id}: Update a user's information.
DELETE /users/{id}: Delete a user.
