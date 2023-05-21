import socket
target_host = "185.229.118.198"
target_port = 80
count = 0
while True:
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the client
    client.connect((target_host,target_port))
    # send some data 

    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    # client.send(b"qanjut")
    # receive some data
    response = client.recv(4096)
    
    
    
    print(response.decode())
    count += 1
    print(count)
    client.close()

