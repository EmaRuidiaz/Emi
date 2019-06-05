import db_connection
from datetime import datetime

class EstacionamientoController:
	def __init__(self, patente):
		self._setingreso()
		self.salida = ""
		self.precio_base = "15"
		self.direccion = ""
		self.patente = patente
		self.dbConn()

	def iniciar_estacionamiento():
		query = "Insert into estacionamiento(ingreso,salida,precio_base,direccion,patente) values()"

		ahora = datetime.now()
		fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
		mat = input(' Ingrese la matricula:\t')
		tiempo = datetime.now()
		matricula.append(mat)
		matricula.append(tiempo)

	def _setingreso(self):
		ahora = datetime.now()
		fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
		self._horaentrada = fecha

	def _getHoraEntrada(self, horaentrada):
		return self._horaentrada

	def _setHoraSalida(self, horasalida):
		self._horasalida = horasalida

	def _getHoraSalida(self):
		return self._horasalida

	def _setMontoTotal(self, montototal):
		self._montototal = montototal

	def _getMontoTotal(self):
		return self._montototal

	def _setDireccion(self, direccion):
		self._direccion = direccion

	def _getDireccion(self):
		return self._direccion

	def iniciar_estacionamiento():
		mat = input(' Ingrese la matricula:\t')
		tiempo = datetime.now()
		matricula.append(mat)
		matricula.append(tiempo)

	def finalizar_estacionamiento():
		mat = input(' Ingrese la matricula:\t')
		if mat in matricula:
			pos = matricula.index(mat)
			pos+= 1
			tiempo = datetime.now()
			tiem_total=tiempo - matricula[pos] 
			print(tiem_total)

	horaentrada = property(fget = _getHoraEntrada, fset = _setHoraEntrada)
	horasalida = property(fget = _getHoraSalida, fset = _setHoraSalida)
	montototal = property(fget = _getMontoTotal, fset = _setMontoTotal)
	direccion = property(fget = _getDireccion, fset = _setDireccion)

	def calculo_monto(self, _getHoraEntrada, _getHoraSalida):
		pass


class UsuarioController:
	def __init__(self):
		self.conn = dbConn()
		self.vista = UsuarioView()
		self.usuario_controller()

	def usuario_controller():
		self.vista.iniciar_sesion()
		

