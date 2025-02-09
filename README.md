# ⛅️ Weather ETL Pipeline

## 🐠 Giới thiệu

Dự án này sử dụng Apache Airflow để thu thập, xử lý và tải dữ liệu thời tiết. Quy trình ETL giúp xử lý dữ liệu thời gian thực và đưa vào hệ thống cơ sở dữ liệu.

## 🌟 Mô hình

- **Dữ liệu thu thập**: Dữ liệu thời tiết từ API

- **Xử lý**: Chuẩn hóa, làm sạch dữ liệu

- **Tải dữ liệu**: Lưu vào PostgreSQL

## 🌍 Công nghệ sử dụng

- **Apache Airflow**: Quản lý DAGs

- **PostgreSQL** : Lưu trữ dữ liệu

- **Docker**: Triển khai pipeline

## 🛠️ Cài đặt & Chạy thừ

### 1. Clone repository

git clone https://github.com/user/weather-etl.git
cd weather-etl

### 2. Cài đặt dependencies

docker-compose up --build

### 3. Kiểm tra DAG trên Airflow

- Mở trình duyệt và truy cập: http://localhost:8080

- Đăng nhập bằng tài khoản mặc định (admin/admin)

- Kích hoạt DAG weather_etl
