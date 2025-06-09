FROM python:3.11-slim

# Cài ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Tạo thư mục app
WORKDIR /app

# Copy toàn bộ code vào container
COPY . .

# Cài thư viện Python từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Chạy ứng dụng Flask
CMD ["python", "main.py"]
