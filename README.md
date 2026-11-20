# Stock Decision Engine — India (NSE/BSE via Zerodha)

India version of the app: same engine as the US repository, configured with
`APP_MARKET=IN`. Its own database (`stockmarket_in`), backend port **8001**,
dashboard port **5174**, so it can run next to the US app.

> Status: analysis only. Orders stay in Zerodha **dry-run** until Kite
> Connect is active and your static IP is registered with Zerodha
> (SEBI/NSE rule since 1 April 2026). Alpaca/US features are off.

## First-time setup (Windows, PowerShell)
```powershell
docker compose up -d                       # same stock-postgres container as the US app
docker exec -it stock-postgres psql -U stockuser -d postgres -c "CREATE DATABASE stockmarket_in OWNER stockuser;"
cd stock-market-backend
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
copy .env.example .env                     # fill in Kite keys and secrets
.\.venv\Scripts\alembic upgrade head
cd ..\stock-market-ui
npm install
```

## Run
```powershell
# backend (from stock-market-backend)
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8001
# dashboard (from stock-market-ui) -> http://localhost:5174
npm run dev
```
Each morning, complete the Zerodha login from the dashboard (Kite tokens
expire daily at 06:00 IST).

## Update
```powershell
git pull
cd stock-market-backend; .\.venv\Scripts\alembic upgrade head
```

## Tests
```powershell
cd stock-market-backend
.\.venv\Scripts\python.exe -m pytest -q
```
