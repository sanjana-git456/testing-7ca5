# DischargeGuard

DischargeGuard is a modern SaaS platform designed for hospitals to manage post-discharge care. It leverages automated symptom monitoring, FHIR-based data integration, and smart scheduling to reduce patient readmission rates.

## Tech Stack
- **Backend**: FastAPI (Python 3.10+), SQLAlchemy, PostgreSQL
- **Frontend**: Vue.js 3, Vite, Pinia, Tailwind CSS
- **Auth**: JWT-based authentication

## Setup

### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example`
4. `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`