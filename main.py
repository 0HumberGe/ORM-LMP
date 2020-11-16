from BackEnd import *

db.connect()
db.create_tables([Alumno])

#INSERT
insertInAlumno('Osvaldo', 'Delgado')
insertInAlumno('Miguel', 'Rocha')
insertInAlumno('Brandon', 'Ibarra')
insertInAlumno('Humberto', 'Peña')
insertInAlumno('Omar', 'Barron')
insertInAlumno('Rolando', 'Dominguez')

'''
'''
print('\n')
ShowData()

#SELECT BY MATRICULA
print('\nSELECT BY MATRICULA')
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByMat(1).nombre, selectByMat(1).apellido, selectByMat(1).matricula))
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByMat(2).nombre, selectByMat(2).apellido, selectByMat(2).matricula))
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByMat(3).nombre, selectByMat(3).apellido, selectByMat(3).matricula))

#SELECT BY NOMBRE
print('\nSELECT BY NOMBRE')
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByName('Miguel').nombre, selectByName('Miguel').apellido, selectByName('Miguel').matricula))
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByName('Humberto').nombre, selectByName('Humberto').apellido, selectByName('Humberto').matricula))
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByName('Brandon').nombre, selectByName('Brandon').apellido, selectByName('Brandon').matricula))

#SELECT BY APELLIDO
print('\nSELECT BY APELLIDO')
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByLastName('Rocha').nombre, selectByLastName('Rocha').apellido, selectByLastName('Rocha').matricula))
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByLastName('Peña').nombre, selectByLastName('Peña').apellido, selectByLastName('Peña').matricula))
print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByLastName('Barron').nombre, selectByLastName('Barron').apellido, selectByLastName('Barron').matricula))

ShowData()
#DELETE BY MATRICULA
print('\nDELETE BY MATRICULA')
DeleteByMat(6)
print('\n')
ShowData()

#DELETE BY NAME
print('\nDELETE BY NOMBRE')
DeleteByName('Humberto')
print('\n')
ShowData()

#DELETE BY APELLIDO
print('\nDELETE BY APELLIDO')
DeleteByLastName('Rocha')
print('\n')
ShowData()
