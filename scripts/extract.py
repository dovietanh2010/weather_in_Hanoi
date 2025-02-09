import requests
import pandas as pd
import os

API_KEY = "cc4ef870e609fbf44351a44826082cda"
CITY = "Hanoi"
URL = f"https://api.openweathermap.org/data/2.5/weather?q=Hanoi&appid={API_KEY}&units=metric"


def extract():
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame([{
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "timestamp": pd.Timestamp.now()
        }])
        df.to_csv("/tmp/weather_data.csv", index=False)
        print("Dữ liệu đã được trích xuất!")
    else:
        print("Lỗi khi trích xuất dữ liệu!")

if __name__ == "__main__":
    extract()
