from db_connection import DBconn
from datetime import datetime
from EmiView import EmiView
from Emi import Usuario

class EstacionamientoController:
	def __init__(self, patente):
		self._setingreso()
		self.salida = ""
		self.precio_base = "15"
		self.direccion = ""
		self.patente = patente

	def iniciar_estacionamiento():
		query = "Insert into estacionamiento(ingreso,salida,precio_base,direccion,patente) values()"

		ahora = datetime.now()
		fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
	


class UsuarioController:
	def __init__(self):
		self.conn = DBconn()
		self.user_view = EmiView()
		self.patente = ""
		self.dni = ""
		self.user = Usuario()
		self.usuario_controller()
		

	def usuario_controller(self):
		(self.patente, self.dni) = self.user_view.iniciar_sesion()
		print(self.patente, "", self.dni)
		datos = self.user.validar(self.patente, self.dni)
		print("Datos de la consulta ",datos)
		if len(datos) != 0:
			self.user_view.confirmar_ingreso()
			self.user_view.mostrar_menu()
		else:
			self.user_view.datos_incorrectos()

persona = UsuarioController()