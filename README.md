#  Fashion Store API (FastAPI Project)
A fully functional backend system for a Fashion Store built using **FastAPI**, implementing core backend concepts like CRUD operations, validation, workflows, and advanced querying.
---
##  Project Objective
This project demonstrates the ability to design and build a real-world backend system using FastAPI, covering:
- RESTful API design
- Data validation with Pydantic
- CRUD operations
- Multi-step workflows
- Search, Sorting, Pagination
- Clean code structure and error handling
---
##  Tech Stack
- **Python**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
---
##  Project Structure
fastapi-fashion-store/
│
├── main.py # Complete FastAPI application
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── screenshots/ # API testing screenshots
---
##  How to Run the Project
### 1. Install dependencies
pip install -r requirements.txt
### 2. Run the server
uvicorn main:app --reload
### 3. Open Swagger UI
http://127.0.0.1:8000/docs
---
##  API Endpoints Overview
###  Basic APIs (Day 1)
- `GET /` → Home route
- `GET /products` → Get all products
- `GET /products/{id}` → Get product by ID
- `GET /products/count` → Total product count
---
###  POST + Validation (Day 2)
- `POST /products` → Create product with validation
---
###  CRUD Operations (Day 4)
- `PUT /products/{id}` → Update product
- `DELETE /products/{id}` → Delete product
---
###  Multi-Step Workflow (Day 5)
**Cart → Order → Checkout**
- `POST /cart` → Add item to cart  
- `GET /cart` → View cart  
- `POST /order` → Place order  
- `PUT /order/{id}/checkout` → Complete order  
---
###  Advanced APIs (Day 6)
- `GET /products/search`
Supports:
-  Keyword Search  
-  Category Filter  
-  Sorting (`price`, `-price`)  
-  Pagination (`page`, `limit`)  
---
##  Features Implemented
-  In-memory database (no external DB)
-  Input validation using Pydantic
-  Proper HTTP status codes (201, 404, 400)
-  Modular helper functions
-  Case-insensitive search
-  Clean API design (static routes before dynamic)
-  Structured workflow logic
---
##  Testing
All APIs are tested using Swagger UI.
Screenshots for each task (Q1–Q20) are stored in the `/screenshots` folder.
---
## Error Handling
- `404 Not Found` → Invalid product/order
- `400 Bad Request` → Invalid operations (e.g., empty cart)
- `422 Unprocessable Entity` → Validation errors
---
##  Future Improvements
- Database integration (MongoDB / PostgreSQL)
- Authentication & Authorization (JWT)
- Payment gateway integration
- Admin dashboard
- Deployment on AWS
---
##  Author
**BOMMINENI PAVAN KUMAR**
---
##  Final Note
This project is not just about building APIs —  
it demonstrates understanding of how backend systems work in real-world applications.

