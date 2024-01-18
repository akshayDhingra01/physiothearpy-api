from fastapi import FastAPI, Query

app = FastAPI()

# Dummy data
dummy_data = [
    {"city": "New York", "population": 8623000, "country": "USA"},
    {"city": "London", "population": 8908081, "country": "UK"},
    {"city": "Tokyo", "population": 13929286, "country": "Japan"},
    # Add more dummy data as needed
]

# GET endpoint with a city parameter
@app.get("/get_data")
async def get_data(city: str = Query(None, title="City", description="The city name to filter data")):
    if city:
        filtered_data = [item for item in dummy_data if item["city"].lower() == city.lower()]
    else:
        filtered_data = dummy_data
    return {"data": filtered_data}
