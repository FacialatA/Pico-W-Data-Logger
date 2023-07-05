import ntptime
import utime

# Configura el servidor NTP
servidor_ntp = "pool.ntp.org"

# Sincroniza el reloj con el servidor NTP
ntptime.host = servidor_ntp
ntptime.settime()

# Obtiene la hora actual
hora_actual = utime.localtime()


