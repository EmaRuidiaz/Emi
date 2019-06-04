from datetime import datetime
matricula = []

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

	patente = property(fget = _getPatente, fset = _setPatente)
	estacionado = property(fget = _getEstacionado, fset = _setEstacionado)
	saldo = property(fget = _getSaldo, fset = _setSaldo)

	def iniciar_estacionamiento():
		self._setPatente = input(' Ingrese la matricula:\t')
		tiempo = datetime.now()
		matricula.append(mat)
		matricula.append(tiempo)

	def finalizar_estacionamiento():
		mat = input(' Ingrese la matricula:\t')
		if mat in matricula:
			pos = matricula.index(mat)
			pos+= 1
			tiempo = datetime.now()
			tiem_total= tiempo - matricula[pos]
			print(tiem_total)
			print(tiem_total)
			print('  Patente: ---> ', mat, '        horario de entrada ---> ', matricula[pos])
			print('                                 horario de salida  ---> ', tiempo)
			print('                                 tiempo transcurrido --> ', tiem_total)


	def consultar_saldo():
		pass

	def consultar_estado():
		pass

	def finalizar_sesion():
		salida = 2
		while salida !=1:
			opcion=int(input('1. Ingresar Patente: \n 2. Dar de baja: \n'))
			if opcion == 1:
				iniciar_estacionamiento()
			else:
				finalizar_estacionamiento()
			salida = int(input('Desea salir   1. Si   2. No'))