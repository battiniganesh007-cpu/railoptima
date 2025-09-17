# RailOptima Prototype

## Run with Docker
```bash
docker-compose up --build
```
- Backend → http://localhost:8000  
- Frontend → http://localhost:3000  

## Run without Docker

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend will run at http://localhost:3000
