from peewee import *

db = SqliteDatabase('Escuela.db')

class Alumno(Model):
    nombre = CharField()
    apellido = CharField()
    matricula = AutoField()
    
    class Meta:
        database = db


