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
#Excepciones personalizados 
class ErrorsistemaFJ(Exception):
    pass

class datosInvalidosError(ErrorsistemaFJ):
    pass

class ParametrofaltanteError(ErrorsistemaFJ):
    pass
class servicioNoDisponibleError(ErrorsistemaFJ):
    pass
class ReservaIncorrectaError(ErrorsistemaFJ):
    pass
class OperacionNoPermitidaError(ErrorsistemaFJ):
    pass
class CalculoIncosistenteError(ErrorsistemaFJ):
    pass
#clases abstractas 

class Entidad(ABC):
    def __init__(self, identidad: int):
        if not isinstance(identidad, int) or identidad <= 0:
            raise datosInvalidosError(f"ID invalido: {identidad}")
        self._identidad
        self._fecha_creacion = datetime.now()

    property
    def id(self):
        return self.__id
    abstractmethod
    def describir(self):
        pass
    abstractmethod
    def validar(self):
        pass
    def __str__(self):
        return self.describir()

#clase de cliente
class Cliente(Entidad):
    def __int__(self, id_cliente, nombre, correo, telefono, documento):
        super().__init__(id_cliente)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.documento = documento
        self.validar()

    property
    def nombre(self):
        return self._nombre

    nombre.setter
    def nombre(self,valor):
        if not valor or len(str(valor).strip())< 3:
            raise datosInvalidosError("El nombre debe tener minimo 3 caracteres")
        self._nombre = str(valor).strip().tittle()

    property
    def correo(self):
        return self.correo

    correo.setter
    def correo(self, valor):
        if not valor or  "@" not in str(valor) or "." not in str(valor):
            raise datosInvalidosError("Correo invalido:" +str(valor))
        self._correo = str(valor).strip().lower()

    property
    def telefono(self):
        return self._telefono

    telefono.setter
    def telefono(self, valor):
        if not re.match(r"^/d{10,10}$", str(valor)):
            raise datosInvalidosError("telefono debe tener de 10 digitos ")
        self._telefono = str(valor)

    property
    def docuemnto(self):
        return self._documento

    docuemnto.setter
    def documento(self, valor):
        if not re.match(r"^/d{8,12}$", str(valor)):
            raise datosInvalidosError("Documentos debe tener de 8 a 12 digitos")
        self._documento = str(valor)

    def validar(self):
        return True

    def describir(self):
        return"Cliente #"
   # clase abstracta servicio
    
class Servicio(Entidad):
    def __init__(self, id_servicio, nombre, precio_base, disponible=True):
        super().__init__(id_servicio)
        if precio_base is None:
            raise ParametrofaltanteError("falta de precio base del servicio")
        if precio_base < 0:
            raise datosInvalidosError("El precio no puede ser negativo")
        self._nombre = nombre 
        self._precio_base = float(precio_base)
        self._disponible = bool(disponible)

    property
    def nombre(self):
        return self._nombre

    property
    def precio_base(self):
        return self._precio_base

    property
    def disponible(self):
        return self._disponible

    disponible.setter
    def disponible(self, valor):
        self._disponible = bool(valor)

    abstractmethod
    def calcular_costo(self, args, kwargs):
        pass

    abstractmethod
    def validar_parametros(self,args,kwargs):
        pass
    def validar(self):
        return self._precio_base >= 0 and bool(self._nombre)
    def describir(self):
        if self._disponible:
            estado = "Disponible"
        else:
            estado = "No disponible"
        return "servicio #"

