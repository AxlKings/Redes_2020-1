#TCPclient
import socket as sock

direccionServidor = "localhost"
puertoServidor = 50366




while True:
    socketCliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    # Se realiza el handshake
    socketCliente.connect((direccionServidor, puertoServidor))
    aEnviar = input("Ingrese la URL: ")
    socketCliente.send(aEnviar.encode())
    if(aEnviar.lower() == "terminate"):
        break
    respuesta = socketCliente.recv(2048).decode()
    
    socketCliente.close()

    socketUDP= sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
    mensajeEnviado= 'OK'
    socketUDP.sendto(mensajeEnviado.encode(), (direccionServidor, int(respuesta)))
    header, _ = socketUDP.recvfrom(2048)
    print("Header recibido: ", header.decode())
    with open(aEnviar+".txt", "w") as arch:
        arch.write(header.decode())
        arch.close()
    socketUDP.close()


