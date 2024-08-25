from fastapi import  FastAPI,HTTPException
app = FastAPI ()
datas = {
    "store_1":{
        "store_id": 1,
        "store_name": "Main Street Store",
        "business_hours": {
            "monday": ["09:00", "18:00"],
            "tuesday": ["09:00", "18:00"],
            "wednesday": ["09:00", "18:00"],
            "thursday": ["09:00", "18:00"],
            "friday": ["09:00", "18:00"],
            "saturday": ["10:00", "16:00"],
            "sunday": []
        },
        "uptime_events": [
            {"start_time": "2024-08-21 09:15:00", "end_time": "2024-08-21 10:00:00"},
            {"start_time": "2024-08-21 11:00:00", "end_time": "2024-08-21 18:00:00"},
            {"start_time": "2024-08-22 09:00:00", "end_time": "2024-08-22 12:30:00"}
        ],
        "downtime_events": [
            {"start_time": "2024-08-21 10:00:00", "end_time": "2024-08-21 11:00:00"},
            {"start_time": "2024-08-22 12:30:00", "end_time": "2024-08-22 13:00:00"}
        ]
    },
    "store_2": {
        "store_id": 2,
        "store_name": "Downtown Store",
        "business_hours": {
            "monday": ["09:00", "18:00"],
            "tuesday": ["09:00", "18:00"],
            "wednesday": ["09:00", "18:00"],
            "thursday": ["09:00", "18:00"],
            "friday": ["09:00", "18:00"],
            "saturday": ["09:00", "14:00"],
            "sunday": []
        },
        "uptime_events": [
            {"start_time": "2024-08-21 09:00:00", "end_time": "2024-08-21 12:00:00"},
            {"start_time": "2024-08-21 13:00:00", "end_time": "2024-08-21 18:00:00"}
        ],
        "downtime_events": [
            {"start_time": "2024-08-21 12:00:00", "end_time": "2024-08-21 13:00:00"}
        ]
    }
}
@app.get("/data")
async def data():
    return datas
@app.get("/{store}")
async def about(store:int):
    store_key = f"store_{store}"
    data = datas.get(store_key)
    if data is None:
        raise HTTPException(status_code=404, detail="Enter a valid store ID")
    
    return data
