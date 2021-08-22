from binascii import a2b_base64
import binascii

def ret_frame(sock):
    #   先接收片数
    length, client = sock.recvfrom(50000)  # 阻塞
    length = int(length.decode('utf-8'))
    #   循环接收bytes
    i = 0
    all_data = ''
    while i < length:
        data_base, client = sock.recvfrom(50000)  # 阻塞
        if data_base == b"":
            sock.close()
            break
        i += 1
        #   bytes转string
        data = data_base.decode('utf-8')
        all_data += data
    #   循环结束，base64转字节流
    #`x = base64.b64decode(all_data)
    return binascii.a2b_base64(all_data)
