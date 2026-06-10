 # 📘 Assignment: Building REST APIs with FastAPI

 ## 🎯 Objective

 Build a simple RESTful API using the FastAPI framework. Students will design CRUD endpoints for a resource, validate input with Pydantic models, and run the service locally with Uvicorn.

 ## 📝 Tasks

 ### 🛠️	Core REST API

 #### Description
 Create a FastAPI application that implements Create, Read, Update, and Delete (CRUD) operations for a single resource (for example, "items" or "notes"). Use Pydantic models for request/response validation and keep data in-memory for the core task.

 #### Requirements
 Completed program should:

 - Use `FastAPI` and `Pydantic` for request handling and validation
 - Expose REST endpoints for: list all resources, get resource by id, create resource, update resource, delete resource
 - Return appropriate HTTP status codes (200/201/204/404 where applicable)
 - Validate request bodies with Pydantic models and return clear error messages for invalid input
 - Include basic in-memory persistence (a Python dict or list) so the API is usable without an external database
 - Provide example requests for each endpoint (curl or HTTPie)

 ### 🛠️	Optional Enhancements

 #### Description
 Improve the API with one or more optional features.

 #### Requirements
 Completed enhancements may include (pick one or more):

 - Persist data to a lightweight database (SQLite) using `SQLModel` or `SQLAlchemy`
 - Add pagination, filtering, or sorting for list endpoints
 - Implement simple authentication (API key or OAuth2 password flow)
 - Add automated tests for endpoints using `pytest` and `httpx`/`starlette` test client
 - Containerize the application with a `Dockerfile` and provide run instructions

 ## Running the starter app

 Install dependencies and run the development server from the assignment folder:

 ```bash
 cd assignments/fastapi-rest-api
 python3 -m pip install -r requirements.txt
 uvicorn starter-code:app --reload
 ```

 Example requests (replace `:8000` if different):

 ```bash
 # List items
 curl http://127.0.0.1:8000/items

 # Create item
 curl -X POST -H "Content-Type: application/json" -d '{"title":"Example","description":"Demo"}' http://127.0.0.1:8000/items

 # Get item
 curl http://127.0.0.1:8000/items/1

 # Update item
 curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated","description":"Changed"}' http://127.0.0.1:8000/items/1

 # Delete item
 curl -X DELETE http://127.0.0.1:8000/items/1
 ```

 ## Deliverables

- A working FastAPI application (starter code provided)
- A short README describing how to run the app and test the endpoints
- (Optional) Any chosen enhancements implemented and documented
