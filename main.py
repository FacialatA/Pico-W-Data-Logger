import conectar_wifi
import abrir_socket
import pagina_web


#Conecto al Wi Fi
conectar_wifi.conectar_wifi()

#Saco la IP de la variable IP global en conectar_wifi.py
ip = conectar_wifi.ip

#Abro un socket en el puerto 80. La funcion retorna informacion del socket que almaceno en la variable coneccion
coneccion = abrir_socket.abrir_socket(ip)

print(ip)
print(coneccion)

# Manejo de solicitudes web
while True:
    # Esperar a que llegue una solicitud
    client_socket, client_address = coneccion.accept()

    # Leer la solicitud del cliente
    request = client_socket.recv(1024).decode()

    # Imprimir la solicitud
    print("Solicitud recibida:")
    print(request)

    # Enviar una respuesta al cliente con el contenido de pagina_web.py
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + pagina_web.html
    client_socket.send(response.encode())

    # Cerrar la conexión con el cliente
    client_socket.close()
