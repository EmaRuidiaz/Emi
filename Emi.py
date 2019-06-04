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

	def estacionar():
		self._setPatente = input(' Ingrese la matricula:\t')
		tiempo = datetime.now()
		matricula.append(mat)
		matricula.append(tiempo)

	def terminar_estacionamiento():
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