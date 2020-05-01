#TCPserver
import socket as suck

def sumar1(cache):
    for url, (header, cont) in cache.items():
        cache[url] = (header , cont+1) 




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

cache = {}

while True:
    for url, (_,cont) in cache.items():
        print(url, cont)
    # Este socket es para comunicarse con el cliente
    # Como conexión es persistente, trabajamos el socket hacia el cliente
    socketCliente, direccionCliente = socketServidor.accept()
    print(socketCliente)
    print(direccionCliente) 
    url = socketCliente.recv(2048).decode()
    print("Se recibió ", url)
    #Ahora debe buscar la url, enviar el puerto de transferencia UDP.

    puertoUDP =50462

    respuesta = str(puertoUDP)
    socketCliente.send(respuesta.encode())
    socketCliente.close()
    
    
    socketServUDP = suck.socket(suck.AF_INET, suck.SOCK_DGRAM)
    socketServUDP.bind(("", puertoUDP))
    xd, clientDir = socketServUDP.recvfrom(2048)
    print("url antes del decode", xd )
    flag = True
  
    header = ''    
    if(url in cache.keys()):
        sumar1(cache)
        tomc, _ = cache[url]
        header= tomc
        cache[url] = (tomc, 0)
    else:
        socketURL = suck.socket(suck.AF_INET, suck.SOCK_STREAM)  
        socketURL.connect((url , 80))
        peticion= "GET / HTTP/1.1\r\nHost:"+ url +"\r\n\r\n"
        socketURL.sendall(peticion.encode())
        cabeza = socketURL.recv(2048).decode(encoding='cp437')    
        socketURL.close()    
        cont = 0
        header=[]
        for line in cabeza.split('\n'):
            header.append(line)
            if(line == '\r' and cont!=0):
                break
            cont += 1
        header = '\n'.join(header)       
        if(len(cache.items()) < 5):
            sumar1(cache)
            cache[url] = (header, 0)
        else:
            maximo = -1
            oldURL = ""
            for fakeURL, (_ , cont) in cache.items():
                if(cont > maximo):
                    maximo = cont
                    oldURL = fakeURL
            del cache[oldURL]
            sumar1(cache)
            cache[url] = (header, 0)
        
    socketServUDP.sendto(header.encode(), clientDir)
    socketServUDP.close()
    
     
