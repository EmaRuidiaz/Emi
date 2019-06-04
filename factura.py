class Factura:
	def __init__(self, horaentrada, horasalida, fecha, monto):
		self._setHoraEntrada(horaentrada)
		self._setHoraSalida(horasalida)
		self._setFecha(fehca)
		self._setMonto(monto)

	def _setHoraEntrada(self, horaentrada):
		self._horaentrada = horaeentrada

	def _getHoraEntrada(self, horaentrada):
		return self._horaentrada

	def _setHoraSalida(self, horasalida):
		self._horasalida = horasalida

	def _getHoraSalida(self):
		return self._horasalida

	def _setFecha(self, fecha):
		self._fecha = fecha

	def _getFecha(self):
		return self._fecha

	def _setMonto(self, monto):
		self._monto = monto

	def _getMonto(self):
		return self._monto

	horaentrada = property(fget = _getHoraEntrada, fset = _setHoraEntrada)
	horasalida = property(fget = _getHoraSalida, fset = _setHoraSalida)
	fecha = property(fget = _getFecha, fset = _setFecha)
	monto = property(fget = _getMonto, fset = _setMonto)