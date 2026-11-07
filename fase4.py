#sistema integral de gestion de clientes, servicios y reservas 
#Software FJ
# sin uso de bases de datos,reservas de
salas, alquiler de equipos y asesorías especializadas

#se crean librerias con ABC abstractmethod para crear clases abstractas, datetime para poner hora y fecha en el log , re expresiones regulares
from abc import ABC, abstractmethod 
from datetime import datetime
import re

#clases derivadas 
class logger :
  ARCHIVO = "errores_y_eventos.log"
  staticmethod
    def registrar(mensaje, nivel="INFORMCION"):
        linea = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{nivel}] {mensaje}\n"
        try:
            with open(Logger.ARCHIVO, "a", encoding="utf-8") as f:
                f.write(linea)
        except OSError as e:
            print(f"No se pudo escribir log: {e}")
        finally:
            
            print(linea.strip())
