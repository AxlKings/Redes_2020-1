#TCPserver
import socket as suck

def sumar1(cache):
    """
    Función para actualizar la antigüedad de los elementos en el cache
    (Se le suma 1 al contador asociado a cada uno)
    """
    for url, (header, cont) in cache.items():
        cache[url] = (header , cont+1) 

"""
El cache funciona de manera que cada url tiene asociado un contador,
siendo el url más reciente el que posee menor valor de contador.
"""
cache = {}
#49152-65535
puertoServidor = 50366
# AF_INET: IPv4
# SOCK_STREAM: TCP
socketServidor = suck.socket(suck.AF_INET, suck.SOCK_STREAM)
socketServidor.bind(("", puertoServidor))
# Indica que espere handshakes, parametro indica
# cantidad maxima de cola
socketServidor.listen(1) # esto es solo para handshakes
print("Servidor TCP escuchando en puerto: ", puertoServidor)
separador = "CAZUELADEPOLLOCONMOSTAZAXD"
try:
    # Se recupera el cache de la ejecución anterior
    archivo = ""
    with open("cache.txt", "r") as arch:
        for linea in arch:
            archivo +=linea
        
        archivo= archivo.split(separador)
        iteraciones = int(len(archivo)/3) 
        inicio=0
        while(iteraciones!=0):
            cache[archivo[inicio]] = (archivo[inicio+1], int(archivo[inicio+2]))
            inicio+=3
            iteraciones-=1
        
except FileNotFoundError:
    # En caso de no existir, se crea
    arch = open("cache.txt", "w")
    arch.close()
while True:
    print("Esperando conexión con cliente")
    url = ""
    # Este socket es para comunicarse con el cliente
    # Como conexión es persistente, trabajamos el socket hacia el cliente
    socketCliente, direccionCliente = socketServidor.accept()
    print("Conexión con cliente iniciada")
    while(url.lower() != "terminate"):

        url = socketCliente.recv(2048).decode()
        if(url != ""):
            print("Se recibió ", url)
        if(url.lower() == "terminate" or url.lower() == ""):
            break
        #Ahora debe buscar la url, enviar el puerto de transferencia UDP.

        puertoUDP =50462

        respuesta = str(puertoUDP)
        socketCliente.send(respuesta.encode())
        
        
        socketServUDP = suck.socket(suck.AF_INET, suck.SOCK_DGRAM)
        socketServUDP.bind(("", puertoUDP))
        ok, clientDir = socketServUDP.recvfrom(2048)
        print(ok.decode())
        flag = True
    
        header = ''    
        # Se revisa si la url está en el cache
        if(url in cache.keys()):
            sumar1(cache)
            tomc, _ = cache[url]
            header= tomc
            cache[url] = (tomc, 0) # Se actualiza su contador en el cache
        else:
            # En caso contrario, se realiza la consulta http
            socketURL = suck.socket(suck.AF_INET, suck.SOCK_STREAM)  
            socketURL.connect((url , 80))
            peticion= "GET / HTTP/1.1\r\nHost:"+ url +"\r\n\r\n"
            socketURL.sendall(peticion.encode())
            cabeza = socketURL.recv(2048).decode(encoding='cp437')    
            socketURL.close()    
            cont = 0
            header=[]
            # Se obtiene solo el header de la respuesta
            for line in cabeza.split('\n'):
                header.append(line)
                if(line == '\r' and cont!=0):
                    break
                cont += 1
            header = '\n'.join(header)       
            if(len(cache.items()) < 5):
                # Se agrega la url al cache en caso de tener menos de 5
                sumar1(cache)
                cache[url] = (header, 0)
            else:
                # En caso contrario, se cambia por la url más antigua
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
        print("Header enviado")
        socketServUDP.close()
    socketCliente.close()
    # Una vez terminada la consulta del cliente, se actualiza el cache.txt
    if(url != ""):
        print("Conexión con cliente finalizada")
        with open("cache.txt", "w") as arch:
            for url, (header, cont) in cache.items():
                arch.write(url+separador+header+separador+str(cont)+separador)
            
     
