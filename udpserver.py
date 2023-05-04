import socket
IP = '192.168.100.173'
PORT = 9997
buffer = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((IP, PORT))
print("SERVER UP")

while True:
    data = server.recvfrom(buffer)
    pesan = data[0]
    ip_addr = data[1]
    print("PESAN DARI CLIENT: \"{}\"".format(pesan))
    print("IP DARI CLIENT: \"{}\"".format(ip_addr))
    server.sendto(b"Welcome To Server Zx", ip_addr)


