import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 0))
assigned_port = server.getsockname()[1]

print(f"Server is running on port {assigned_port}")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=int(input("Enter load balancer port:"))
ip=input("Enter ip:")
client.connect((ip, port)) 
server.listen(5)

while True:
    data = client.recv(1024)
    print(f"Received request:{data}")
    if not data:
        break
    data= int(data.decode())
    ans=1;
    while data>0:
        ans*=2
        data-=1
    ans=str(ans)
    client.sendall(ans.encode())

