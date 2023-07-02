import conectar_wifi
import abrir_socket

#Conecto al Wi Fi
conectar_wifi.conectar_wifi()
#Saco la IP de la variable IP global en conectar_wifi.py
ip = conectar_wifi.ip

#Abro un socket en el puerto 80. La funcion retorna informacion del socket que almaceno en la variable coneccion
coneccion = abrir_socket.abrir_socket(ip)

print(ip)
print(coneccion)
