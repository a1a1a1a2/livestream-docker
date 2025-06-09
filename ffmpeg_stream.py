import subprocess, os

def start_stream():
    input_file = "sample.mp4"
    if not os.path.exists(input_file):
        print("⚠️ Không có sample.mp4")
        return
    # Thay YOUR_STREAM_KEY bằng key YouTube thật
    cmd = [
        "ffmpeg", "-re", "-stream_loop", "-1",
        "-i", input_file,
        "-c:v", "libx264", "-preset", "veryfast",
        "-c:a", "aac", "-b:a", "128k",
        "-f", "flv",
        "rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY"
    ]
    subprocess.Popen(cmd)
    print("✅ Livestream đã bắt đầu")
