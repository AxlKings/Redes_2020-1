#TCPserver
import socket as suck

#49152-65535
puertoServidor = 50366
# AF_INET: IPv4
# SOCK_STREAM: TCP
socketServidor = suck.socket(suck.AF_INET, suck.SOCK_STREAM)
socketServidor.bind(("", puertoServidor))
# Indica que espere handshakes, parametro indica
# cantidad maxima de cola
socketServidor.listen(1) # esto es solo para handshakes XD
print("Servidor TCP escuchando en puerto: ", puertoServidor)

while True:
    # Este socket es para comunicarse con el cliente
    # Como conexión es persistente, trabajamos el socket hacia el cliente
    socketCliente, direccionCliente = socketServidor.accept()
    print(socketCliente)
    print(direccionCliente) 
    mensaje = socketCliente.recv(2048).decode()
    print("Se recibió ", mensaje)
    #Ahora debe buscar la url, enviar el puerto de transferencia UDP.

    puertoUDP =50462

    respuesta = puertoUDP
    socketCliente.send(respuesta.encode())
    socketCliente.close()
    

    socketServUDP = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
    socketServUDP.bind(("", puertoUDP))
    mensaje, clientDir = socketSocketServUDP.recvfrom(2048)

    
