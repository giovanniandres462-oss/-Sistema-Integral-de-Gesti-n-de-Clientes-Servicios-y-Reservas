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
  
