from flask import Flask, render_template, Response
from frame_base import ret_frame


def get_frame():
    image_bytes = ret_frame()
    return image_bytes


app = Flask(__name__)


@app.route('/')  # 主页
def index():
    return render_template('index.html')


#   获得帧字节流
def gen():
    while True:
        frame_bytes = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


#   传递帧
@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(
        host='192.168.101.8',
        port=5000,
        debug=True
    )

