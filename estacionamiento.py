import datetime 

class Estacionamiento:
	def __init__(self, horaentrada, horasalida, montototal, direccion):
		self._setHoraEntrada(horaentrada)
		self._setHoraSalida(horasalida)
		self._setMontoTotal(montototal)
		self._setDireccion(direccion)

	def _setHoraEntrada(self, horaentrada):
		self._horaentrada = horaeentrada

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

	horaentrada = property(fget = _getHoraEntrada, fset = _setHoraEntrada)
	horasalida = property(fget = _getHoraSalida, fset = _setHoraSalida)
	montototal = property(fget = _getMontoTotal, fset = _setMontoTotal)
	direccion = property(fget = _getDireccion, fset = _setDireccion)

	def calculo_monto(self, _getHoraEntrada, _getHoraSalida):
