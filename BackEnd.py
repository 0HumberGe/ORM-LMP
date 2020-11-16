from peewee import *
import sqlite3
from dbModel import *

db.connect()

def select(colum, mat):
    exam = Alumno.get(colum = mat)
    print(exam.nombre,exam.apellido, 'con matricula ', exam.matricula, 'es culon')

select(, 1)


'''
select(3)
select(4)
select(5)

conn = sqlite3.connect('Escuela.db')
cur = conn.cursor()

cur.execute('SELECT * FROM alumno')
select = cur.fetchall()
print(select)
alumno = Alumno.select().where(Alumno.matricula=='12')[0]
print(Alumno.nombres)
print(alumno)
db.
'''