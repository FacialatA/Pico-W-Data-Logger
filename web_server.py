import network
import socket
import utime
import machine

ssid = "Andá Pallá Bobo"
password = "Invitado$14"

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        utime.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection
    
try:
    ip = connect()
    connection = open_socket(ip)
except KeyboardInterrupt:
    machine.reset()





    
# Creo una variable para el led de la pi pico y una función para que parpadee
#led = machine.Pin("LED", machine.Pin.OUT)

#def parpadeo():
#    while True:
#        led.on()
#        utime.sleep(1)
#        led.off()
#        utime.sleep(1)


#parpadeo()
