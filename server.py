import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Taxi Rechytsa API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

drivers_db = [
    {
        "telegram_id": 123456789,  # Замените на реальный ID Кости (@userinfobot)
        "name": "Костя (Шурин)",
        "phone": "+375 (29) 111-22-33",
        "car_model": "Volkswagen Polo",
        "car_number": "3-TAP-1234",
        "rating": 4.95,
        "is_active": True
    }
]

@app.get("/api/driver/{telegram_id}")
def get_driver_by_tg(telegram_id: int):
    for driver in drivers_db:
        if driver["telegram_id"] == telegram_id and driver["is_active"]:
            return driver
    raise HTTPException(status_code=404, detail="Водитель не найден")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
