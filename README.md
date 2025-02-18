## 1️⃣ Install Dependencies

### Backend (Python & FastAPI)
```sh
cd backend
pip install -r requirements.txt
```

### Frontend (React/Next.js)
```sh
cd frontend
npm install
```

## 2️⃣ Set Up Environment Variables

### Backend
Create a `.env` file inside the `backend/` directory and add:

```ini
DATABASE_URL=postgresql://username:password@localhost:5432/duckpays
RAZORPAY_API_KEY=your_razorpay_key
OTP_SERVICE_API=your_otp_service_api
```

### Frontend
Create a `.env.local` file inside the `frontend/` directory and add:

```ini
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## 3️⃣ Run the Application

### Start Backend (FastAPI)
```sh
cd backend
uvicorn main:app --reload
```

### Start Frontend (React)
```sh
cd frontend
npm run dev
```

## 4️⃣ Access the Website

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)
- Database: Connect PostgreSQL using `DATABASE_URL`
```
