import socket

print("Started the server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(1024)
    if not data:
        break
    print("Received some date: {}".format(data))
    conn.sendall(b'<!>test')
conn.close()