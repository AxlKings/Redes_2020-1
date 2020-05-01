#TCPclient
import socket as sock

direccionServidor = "localhost"
puertoServidor = 50366

socketCliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
# Se realiza el handshake
socketCliente.connect((direccionServidor, puertoServidor))



aEnviar = input("Ingrese la URL: ")
socketCliente.send(aEnviar.encode())
respuesta = socketCliente.recv(2048).decode()
print("Respuesta: ", respuesta)
socketCliente.close()