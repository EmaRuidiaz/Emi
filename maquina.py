from Usuario_Registrado import *


class Maquina:
	def __init__(self, Id, papel, fecha, hora ):
		self._setId(Id)
		self._setPapel(papel)
		self._setfecha(fecha)
		self._setHora(hora)

	def _setId(self, id):
		self._id = Id

	def _getId(self):
		return self._id

	def _setPapel(self, papel):
		self._papel = papel

	def _getPapel(self):
		return self._papel

	def _setFecha(elf, fecha):
		self._fecha = fecha

	def _getFecha(self):
		return self._fecha

	def _setHora(self, hora):
		self._hora = hora

	def _getHora(self):
		return self._hora

	Id = property(fget= _getId, fset = _setId)
	papel = property(fget = _getPapel, fset = _setPapel)
	fecha = property(fget = = _getFecha, fset = _setFecha)
	hora = property(fget = _getHora, fset = _setHora)

	def imprimir_factura():
		print

	#def iniciar_estacionamiento():

	#def finalizar_estacionamiento():

	def mostrar_saldo():
		pass
	def verificar-cuenta():
		pass