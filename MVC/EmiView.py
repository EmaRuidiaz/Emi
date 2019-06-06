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

			Opcion: """
		opcion = input(menu)
		return opcion

	def iniciar_sesion(self):
		patente = str(input("Ingrese su patente: "))
		dni = input("Ingrese su dni: ")
		return (patente,dni)

	def confirmar_ingreso(self):
		print("Inicio Correcto")

	def datos_incorrectos(self):
		print("Error! Datos Incorrectos")

