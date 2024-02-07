import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=int(input("Enter load balancer port:"))
ip=input("Enter ip:")
client.connect((ip, port))
while True:
    n=input("Enter a number (client1):")
    if not n:
        break
    client.sendall(n.encode()) 
    ans=client.recv(1024).decode()
    print(f"2 power {n} is {ans}")
