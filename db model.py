from peewee import *

db = SqliteDatabase('gente.db')

class Alumno(Model):
    nombres = CharField()
    apellidos = CharField()
    matricula = CharField()   
    
    class Meta:
        database = db

db.connect()
db.create_tables([Alumno])


Maik = Alumno.create(nombres='Miguel', apellidos='Rocha', matricula='12')
Beto = Alumno.create(nombres='Humberto', apellidos='Peña', matricula='13')
Omar = Alumno.create(nombres='Omar', apellidos='Barron', matricula='14')


alumno = Alumno.select().where(Alumno.matricula == '12').get()
print(alumno.nombres)