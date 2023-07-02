import network

# Inicializar el objeto WLAN (WiFi) en la Raspberry Pi Pico W
wlan = network.WLAN(network.STA_IF)

#FUNCION PARA CONECTAR AL WIFI
def conectar_wifi():
    # Importar las variables red y password desde el archivo red.py
    import red
    
    # Obtener el nombre de la red y la contraseña
    nombre_red = red.red
    contraseña = red.password
    
    # Verificar si la conexión ya está activa
    if wlan.isconnected():
        print("La Raspberry Pi Pico W ya está conectada a una red WiFi.")
        return
    
    # Conectar a la red WiFi
    print("Conectando a la red WiFi: {}".format(nombre_red))
    wlan.active(True)
    wlan.connect(nombre_red, contraseña)
    
    # Esperar hasta que se establezca la conexión
    while not wlan.isconnected():
        pass
    
    # Obtener la dirección IP asignada
    ip = wlan.ifconfig()[0]
    
    # Imprimir información de la conexión exitosa
    print("Conexión WiFi establecida.")
    print("Dirección IP: {}".format(ip))
    
ip = wlan.ifconfig()[0]

