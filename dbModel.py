from peewee import *

db = SqliteDatabase('Escuela.db')

class Alumno(Model):
    nombre = CharField()
    apellido = CharField()
    matricula = AutoField()
    
    class Meta:
        database = db

#db.connect()
#db.create_tables([Alumno])

'''
Maik= Alumno.create(nombre='Miguel', apellido='Rocha')
Beto = Alumno.create(nombre='Humberto', apellido='Peña')
Omar = Alumno.create(nombre='Omar', apellido='Barron')
Brandon = Alumno.create(nombre='Brandon', apellido='Ibarra')
'''