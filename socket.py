import socket
ip_port = ('47.107.239.20',8888)

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(sk.connect(ip_port))

recvdata = sk.recv(1024)
print(str(recvdata,encoding='utf8')) # 接收消息 recvdata 是bytes形式的，所以转化为 str

content = "B"*400000000
sk.sendall(bytes(content+"\x00\x00\x0d\x0a",encoding="utf8"))   #\x00\x00\x0d\x0a表达结束，发送消息也是bytes

recvdata = sk.recv(1024)
print(str(recvdata,encoding='utf8'))

sk.close()
