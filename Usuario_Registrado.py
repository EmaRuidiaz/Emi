class UsuarioRegistrado:
	def __init__(self, patente, saldo, estacionado=false):
		self._setPatente(patente)
		self._setEstacionado(estacionado)
		self._setSaldo(saldo)

	def _setPatente(self, patente):
		self._patente = patente

	def _getPatente(self):
		return self._patente

	def _setEstacionado(self, estacionado):
		self._estacionado = estacionado

	def _getEstacionado(self):
		return self._estacionado

	def _setSaldo(self, saldo):
		self._saldo = saldo

	def _getSaldo(self):
		return self._saldo

	def iniciar_estacionamiento():
		pass

	def finalizar_estacionamiento():
		pass

	def consultar_saldo():
		pass

	def consultar_estado():
		pass

	def finalizar_sesion():
		pass