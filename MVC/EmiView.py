class EmiView:

	def __init__(self):
		pass

	def mostrar_menu(self):
		menu = """
		Menu del Emi
			(1) Iniciar Estacionamiento
			(2) Terminar Estacionamiento
			(3) Consultar Saldo

			(4) Salir
		"""
		opcion = input(menu)
		return opcion

	def iniciar_sesion(self):
		spatente = raw_input("Ingrese su patente: ")
		dni = input("Ingrese su dni: ")
		return patente,dni



x = EmiView()
x.iniciar_sesion()