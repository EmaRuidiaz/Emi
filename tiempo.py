from datetime import datetime
"""
mat = []
matricula= input('ingrese nombre de matricula: ')
mat.append(matricula)
x = datetime.now()
print(x)

matricula= input('ingresar nombre matricula para dar de baja: ')
if matricula in mat:
	a = datetime.now()
	print(a)
	z = a-x
	print(z)
else:
	print('no se encentra registrado')
"""

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

matricula = []
salir=2
while salir != 1:
	opcion=int(input(' 1. Desea ingresar patente \n 2. Desea buscar patente\n'))
	if opcion == 1:
		iniciar_estacionamiento()
	else:
		finalizar_estacionamiento()
		print('  Patente: ---> ', mat, '        horario de entrada ---> ', matricula[pos])
		print('                                 horario de salida  ---> ', tiempo)
		print('                                 tiempo transcurrido --> ', tiem_total)

	salir=int(input('desea salir  1. Si  2. No'))