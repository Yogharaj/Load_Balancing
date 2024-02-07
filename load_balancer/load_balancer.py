import socket
import threading
import time
c=0
def get_ip_address():
    hostname = socket.gethostname()    
    ip_address = socket.gethostbyname(hostname)
    return ip_address
def handle_client(client_socket, client_address,l1):
    print(f"Connection from {client_address}")
    global c
    n=l1
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received client request from {client_address}")
        time.sleep(2)
        print(f"Routing request to server {c+1}...")
        l1[c].sendall(data.encode())
        ans=l1[c].recv(1024).decode()
        client_socket.sendall(ans.encode())
        c=(c+1)%2
        

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 0))
assigned_port = server.getsockname()[1]
ip=get_ip_address()



print(f"Load Balancer is running on {ip}:{assigned_port}")
server.listen(5)
l1=list()

n=2
while n>0:
    client, addr = server.accept()
    print(f"Load Balancer Connection from {addr} has been established.")
    l1.append(client)
    n-=1

while True:
    client, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client, addr,l1))
    client_thread.start()

    
    
    
    