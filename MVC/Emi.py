import datetime 
from db_connection import DBconn

class Estacionamiento:
	def __init__(self, horaentrada, horasalida, montototal, direccion):
		self.db = DBconn()


class Factura:
	pass


class Maquina:
	pass

class Usuario:
	def __init__(self):
		self.patente = ""
		self.dni = ""
		self.nombre = ""
		self.saldo = ""
		self.db = DBconn()

	def validar(self):
		query = "Select dni from usuario where patente = %s and dni = %s"
		values = (self.patente, self.dni)
		return self.db.ejecutar(query,values)