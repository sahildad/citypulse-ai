from fastapi import FastAPI, HTTPException

from app.services.weather import get_weather
from app.config.cities import cities as CITIES


app = FastAPI(
    title="CityPulse AI",
    description="AI-powered urban intelligence platform",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "project": "CityPulse AI",
        "status": "running"
    }


@app.get("/api/city/{city_name}/weather")
def city_weather(city_name: str):

    city_name = city_name.lower()

    if city_name not in CITIES:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    city = CITIES[city_name]

    weather_data = get_weather(
        city["latitude"],
        city["longitude"]
    )

    return {
        "city": city["name"],
        "country": city["country"],
        "weather": weather_data
    }