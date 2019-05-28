from datetime import datetime
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
