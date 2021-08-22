from flask import Flask, render_template, Response
from frame_base import ret_frame
import socket

base_add = ('192.168.43.52', 56565)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(base_add)

app = Flask(__name__)
@app.route('/')  # 主页
def index():
    return render_template('index.html')

#   传递帧
@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def get_frame():
    image_bytes = ret_frame(sock)
    return image_bytes

#   获得帧字节流
def gen():
    while True:
        frame_bytes = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8798
    )

