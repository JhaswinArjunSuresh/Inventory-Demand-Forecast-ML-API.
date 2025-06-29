# 📦 Inventory Demand Forecast ML API

Predicts next 7 days demand for SKUs based on recent sales.

## Endpoints
- `POST /forecast` with `{ "sku": "A001", "recent_sales": [20,22,19,23,21,18,20] }`
- `GET /health`

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

