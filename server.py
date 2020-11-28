from socket import *
import os

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(('localhost',int(os.getenv('PORT'))))
    serversocket.listen(5)
    while(1):
        clientsocket, address = serversocket.accept()
        message = clientsocket.recv(4096)
        path = message.split()[1]
        
        if path == b"/admin":
            msg = "HTTP/1.1 200 OK\n Content-Type: text/html \n\n <html><body>This is admin page, no one should be here</body></html>\n"
            clientsocket.send(msg.encode())
        else:
            msg = f"HTTP/1.1 200 OK\n Content-Type: text/html \n\n <html><body>Hello from server ID={str(os.getenv('PORT'))} </body></html>\n"
            clientsocket.send(msg.encode())

        clientsocket.shutdown(SHUT_WR)
        clientsocket.close()

    serversocket.close()

createServer()