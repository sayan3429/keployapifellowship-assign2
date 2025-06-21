# keployapifellowship-assign2
Name Analyzer API Project
A custom API built with FastAPI, offering fun and unique name analysis features. This project demonstrates API design, database integration, and a simple frontend for user interaction.

APIs and Their Functionality
This project exposes several API endpoints for creating, retrieving, updating, and deleting name analyses:

POST /analyze

Functionality: Analyzes a new name and stores the result in the database.

Input: {"name": "Alice"}

Output: Returns analysis, personality score, and lucky number for the provided name.

GET /analyses

Functionality: Retrieves all stored name analyses (with pagination).

Output: List of all analyses.

GET /analyses/{analysis_id}

Functionality: Retrieves a specific analysis by ID.

Output: Single analysis data.

PUT /analyses/{analysis_id}

Functionality: Updates an existing analysis.

Input: JSON with updated fields.

Output: Updated analysis data.

DELETE /analyses/{analysis_id}

Functionality: Deletes a specific analysis by ID.

Output: Confirmation message.

GET /analyze/{name}

Functionality: Retrieves analysis for a specific name.

Output: Analysis data for the name.

Database Integration
Database Used: SQLite (local file-based database for simplicity and ease of setup).

Integration:

All API endpoints interact with the database to store and retrieve name analyses.

The database is initialized and managed using SQLAlchemy ORM.

Database tables are created automatically on server startup.

Each analysis includes name, analysis text, personality score, lucky number, and creation timestamp.

How to Run Your Server
Install dependencies:

bash
pip install fastapi uvicorn sqlalchemy
Navigate to your project directory:

bash
cd /path/to/your/project
Start the FastAPI server:

bash
uvicorn main:app --reload
Open the interactive API documentation:

text
http://localhost:8000/docs
How to Run Your Frontend Locally (Optional)
Make sure your FastAPI server is running as above.

Place your frontend files (HTML, JS, CSS) in a static directory.

Add the following to your main.py to serve static files:

python
from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="static", html=True), name="static")
Restart your server and open the frontend:

text
http://localhost:8000/
How to Interact with Your API
Sample Requests and Responses
Analyze a New Name

Request:

bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'
Response:

json
{
  "name": "alice",
  "analysis": "Your name suggests creativity and artistic talent.",
  "personality_score": 7.5,
  "lucky_number": 42,
  "id": 1,
  "created_at": "2025-06-21T12:34:56.789Z"
}
Get All Analyses

Request:

bash
curl "http://localhost:8000/analyses"
Response:

json
[
  {
    "name": "alice",
    "analysis": "Your name suggests creativity and artistic talent.",
    "personality_score": 7.5,
    "lucky_number": 42,
    "id": 1,
    "created_at": "2025-06-21T12:34:56.789Z"
  }
]
Get Analysis by Name

Request:

bash
curl "http://localhost:8000/analyze/alice"
Response:

json
{
  "name": "alice",
  "analysis": "Your name suggests creativity and artistic talent.",
  "personality_score": 7.5,
  "lucky_number": 42,
  "id": 1,
  "created_at": "2025-06-21T12:34:56.789Z"
}
Summary
This project showcases API development with FastAPI, database integration with SQLite, and a simple frontend for user interaction. It is easy to run and extend for further experimentation and learning
