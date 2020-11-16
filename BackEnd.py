from dbModel import *
from peewee import *

#INSERT INTO TABLE

def insertInAlumno(name, lastName):
    try:
        Alumno.create(nombre=name,
                     apellido=lastName)
        print('Alta exitosa')
    except:
        print('Algo salio mal')

#SELECT BY MATRICULA
def selectByMat(mat):
    cursor = Alumno.select().where(Alumno.matricula==mat)[0]
    return cursor

#SELECT BY NOMBRE
def selectByName(name):
    cursor = Alumno.select().where(Alumno.nombre==name)[0]
    return cursor

#SELECT BY APELLIDO
def selectByLastName(lastN):
    cursor = Alumno.select().where(Alumno.apellido==lastN)[0]
    return cursor

#DELETE BY MATRICULA
def DeleteByMat(mat):
    print('Borrando Registro de:')
    print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByMat(mat).nombre, selectByMat(mat).apellido, selectByMat(mat).matricula))
    try:
        cursor = Alumno.get(matricula=mat)
        cursor.delete_instance()
        print('Baja Exitosa')
    except:
        print('Algo salio mal')

#DELETE BY NOMBRE
def DeleteByName(name):
    print('Borrando Registro de:')
    print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByName(name).nombre, selectByName(name).apellido, selectByName(name).matricula))
    try: 
        cursor = Alumno.get(nombre=name)
        cursor.delete_instance()
        print('Baja Exitosa')
    except:
        print('Algo salio mal')

#DELETE BY APELLIDO
def DeleteByLastName(lastN):
    print('Borrando Registro de:')
    print('Nombre: {}, Apellido: {}, Matricula: {}'.format(selectByLastName(lastN).nombre, selectByLastName(lastN).apellido, selectByLastName(lastN).matricula))
    try: 
        cursor = Alumno.get(apellido=lastN)
        cursor.delete_instance()
        print('Baja Exitosa')
    except:
        print('Algo salio mal')

#Mostrar todos los datos
def ShowData():
    print('\nDatos en la Base de Datos Actualmente')
    for row in Alumno.select():
        print('Nombre: {}, Apellido: {}, Matricula: {}'.format(row.nombre, row.apellido, row.matricula))