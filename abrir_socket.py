import socket

def abrir_socket(ip):
    # Abrir un socket
    direccion = (ip, 80)
    
    # Intentar enlazar el socket al puerto 80
    try:
        coneccion = socket.socket()
        coneccion.bind(direccion)
        coneccion.listen(1)
        return coneccion
    except OSError:
        return "El socket está abierto en el puerto 80"


    