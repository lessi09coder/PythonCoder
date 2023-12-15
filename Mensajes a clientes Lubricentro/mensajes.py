import pywhatkit 
import datetime

# Número de teléfono (con el código de país pero sin el signo +)
""" telefono = "+542364341797" """
telefono = "+542355530757"



# Mensaje que deseas enviar
mensaje = "¡Hola! Este es un mensaje enviado desde Python usando pywhatkit.124241"

# Hora a la que quieres enviar el mensaje (formato: HH, MM)
hora_envio = datetime.datetime.now().hour  # Hora actual
minuto_envio = datetime.datetime.now().minute + 1  # Suma un minuto para el envío



# Enviar el mensaje
pywhatkit.sendwhatmsg(telefono, mensaje, hora_envio, minuto_envio, 15) 

""" for numero in numeros:
    kit.sendwhatmsg(numero, mensaje, hora_envio, minuto_envio)
    time.sleep(20)  # Retraso de 20 segundos entre cada mensaje """