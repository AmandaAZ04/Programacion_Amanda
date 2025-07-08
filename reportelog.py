import logging


#CONFIGURACION BASICA DE LOGGING
logging.basicConfig(
    filename = "reporte.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    encoding = "utf-8"
)

#usuarios del sistema
dict_usuarios = {
    "jdiaz" : "casaca",
    "acid" : "clave123",
    "mperez" : "contraseña"
}

def control_acceso():
    cuenta = input("Usuario: ")
    clave = input("Contraseña: ")

    if cuenta in dict_usuarios:
        if clave == dict_usuarios[cuenta]:
            print("Acceso concedido")
            logging.info(f"Ha ingresado el usuario {cuenta}")
        else:
            print("Contraseña incorrecta")
            logging.warning(f"El usuario {cuenta} se equivocó en la contraseña")
    else:
        print("Cuenta no existe")
        logging.error(f"Se ha intentado ingresar con usuario {cuenta} inexistente")

#PP
try:
    control_acceso()
except KeyboardInterrupt:
    print("Se detectó uso de Ctrl-C. Adiós")
    logging.exception("El programa terminó abruptamente por Ctrl-C")
except Exception as error:
    print("Ocurrio un error. No acecto")
    logging.exception("Ocurrió una excepción")