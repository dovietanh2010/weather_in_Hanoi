import pandas as pd
import psycopg2

DB_CONFIG = {
    "dbname": "airflow",
    "user": "airflow",
    "password": "airflow",
    "host": "postgres",
    "port": 5432
}

def load():
    df = pd.read_csv("/tmp/weather_cleaned.csv")

    # Kết nối PostgreSQL
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Tạo bảng nếu chưa có
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            wind_speed REAL,
            timestamp TIMESTAMP(0)
        )
    """)

    # Chèn dữ liệu vào PostgreSQL
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO weather_data (city, temperature, humidity, wind_speed, timestamp) VALUES (%s, %s, %s, %s, %s)",
            (row['city'], row['temperature'], row['humidity'], row['wind_speed'], row['timestamp'])
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("Dữ liệu đã được tải vào PostgreSQL!")

if __name__ == "__main__":
    load()
