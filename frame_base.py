import base64
import socket

base_add = ('192.168.101.8', 8338)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(base_add)


def ret_frame():
    #   先接收大小
    blength, client = sock.recvfrom(5)
    #   循环接收
    length_str = blength.decode('utf-8')
    length = int(length_str)
    i = 0
    base_data = ''
    while i < length:
        data, client = sock.recvfrom(50000)  # 阻塞
        i += 1
        if data == b"":
            sock.close()
            break
        data = data.decode('utf-8')
        base_data += data
    #   循环结束，base64转字节流
    x = base64.b64decode(base_data)
    return x
