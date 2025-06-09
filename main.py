from flask import Flask
from threading import Thread
from ffmpeg_stream import start_stream

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Bot livestream đang chạy"

@app.route("/start")
def start():
    # Cho phép bật stream thủ công qua /start nếu muốn
    Thread(target=start_stream).start()
    return "🎬 Đã bắt đầu livestream!"

# Tự động khởi động stream khi app bắt đầu
def auto_start_stream():
    Thread(target=start_stream).start()

if __name__ == "__main__":
    auto_start_stream()  # Gọi stream khi Flask khởi động
    app.run(host="0.0.0.0", port=10000)
