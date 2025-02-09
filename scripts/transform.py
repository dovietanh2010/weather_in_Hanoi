import pandas as pd

def transform():
    df = pd.read_csv("/tmp/weather_data.csv")
    
    # Loại bỏ giá trị NULL
    df.dropna(inplace=True)

    # Lưu dữ liệu đã làm sạch
    df.to_csv("/tmp/weather_cleaned.csv", index=False)
    print("Dữ liệu đã được làm sạch!")

if __name__ == "__main__":
    transform()
