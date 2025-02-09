# 🌦️ Weather ETL Pipeline

## 📌 Mô tả

Dự án Weather ETL Pipeline giúp thu thập, xử lý và tải dữ liệu thời tiết vào hệ thống lưu trữ.

## ⚙️ Cách chạy dự án

### Clone repository

git clone https://github.com/user/weather-etl.git
cd weather-etl

### Chạy pipeline với Docker

docker-compose up

### Kiểm tra DAG trên Airflow

Mở trình duyệt và truy cập: http://localhost:8080

Đăng nhập bằng tài khoản mặc định (airflow/airflow)

Kích hoạt DAG weather_etl

## 👌 Mô tả quy trình ETL

Extract: Thu thập dữ liệu thời tiết từ API

Transform: Làm sạch và chuẩn hóa dữ liệu

Load: Tải dữ liệu vào cơ sở dữ liệu

## 📄 Yêu cầu hệ thống

Python 3.8+

Docker & Docker Compose

Apache Airflow

🛠️ Góp ý & Liên hệNếu có bất kỳ câu hỏi hoặc góp ý nào, vui lòng tạo Issue hoặc liên hệ qua email: your.email@example.com.

Chúc bạn cài đặt thành công! 🚀

