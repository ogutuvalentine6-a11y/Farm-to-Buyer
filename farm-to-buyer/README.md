# Farm-to-Buyer Coordination System

An agricultural marketplace connecting farmers, buyers, agrovet owners,
transporters, and traditional knowledge contributors.

## Stack
- FastAPI
- MongoDB (Beanie + Motor)
- JWT auth
- M-Pesa (Daraja)
- AI assistant via secure backend

## Run
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload
