# keployapifellowship-assign2


# Name Analyzer API Project

A custom API built with FastAPI, offering fun and unique name analysis features. This project demonstrates API design and database integration.

---

## **APIs and Their Functionality**

This project exposes several API endpoints for creating, retrieving, updating, and deleting name analyses:

- **POST `/analyze`**  
  - **Functionality:** Analyzes a new name and stores the result in the database.
  - **Input:** `{"name": "Alice"}`
  - **Output:** Returns analysis, personality score, and lucky number for the provided name.
- **GET `/analyses`**  
  - **Functionality:** Retrieves all stored name analyses (with pagination).
  - **Output:** List of all analyses.
- **GET `/analyses/{analysis_id}`**  
  - **Functionality:** Retrieves a specific analysis by ID.
  - **Output:** Single analysis data.
- **PUT `/analyses/{analysis_id}`**  
  - **Functionality:** Updates an existing analysis.
  - **Input:** JSON with updated fields.
  - **Output:** Updated analysis data.
- **DELETE `/analyses/{analysis_id}`**  
  - **Functionality:** Deletes a specific analysis by ID.
  - **Output:** Confirmation message.
- **GET `/analyze/{name}`**  
  - **Functionality:** Retrieves analysis for a specific name.
  - **Output:** Analysis data for the name.

---

## **Database Integration**

- **Database Used:** SQLite (local file-based database for simplicity and ease of setup).
- **Integration:**  
  - All API endpoints interact with the database to store and retrieve name analyses.
  - The database is initialized and managed using SQLAlchemy ORM.
  - Database tables are created automatically on server startup.
  - Each analysis includes name, analysis text, personality score, lucky number, and creation timestamp.

---

## **How to Run Your Server**

1. **Install dependencies:**
pip install fastapi uvicorn sqlalchemy
2. **Navigate to your project directory:**
cd /path/to/your/project
3. **Start the FastAPI server:**
uvicorn main:app --reload
4. **Open the interactive API documentation:**
http://localhost:8000/docs

---


---

## **How to Interact with Your API**

### **Sample Requests and Responses**

- **Analyze a New Name**
- **Request:**
 ```
 curl -X POST "http://localhost:8000/analyze" \
   -H "Content-Type: application/json" \
   -d '{"name": "Alice"}'
 ```
- **Response:**
 ```
 {
   "name": "alice",
   "analysis": "Your name suggests creativity and artistic talent.",
   "personality_score": 7.5,
   "lucky_number": 42,
   "id": 1,
   "created_at": "2025-06-21T12:34:56.789Z"
 }
 ```

- **Get All Analyses**
- **Request:**
 ```
 curl "http://localhost:8000/analyses"
 ```
- **Response:**
 ```
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
 ```

- **Get Analysis by Name**
- **Request:**
 ```
 curl "http://localhost:8000/analyze/alice"
 ```
- **Response:**
 ```
 {
   "name": "alice",
   "analysis": "Your name suggests creativity and artistic talent.",
   "personality_score": 7.5,
   "lucky_number": 42,
   "id": 1,
   "created_at": "2025-06-21T12:34:56.789Z"
 }
 ```

---

