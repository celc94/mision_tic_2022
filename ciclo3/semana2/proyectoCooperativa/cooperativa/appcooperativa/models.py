from ast import mod
from django.db import models #las tablas se crean directamente en app

# Create your models here.
class Cliente(models.Model): #Hereda unas funciones de una superclase Model
#Atributos de la clase
    documento = models.IntegerField(primary_key=True) #Llave Primaria
    nombre = models.CharField(max_length=30) #30 caracteres
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=20)
    celular = models.CharField(max_length=15)
    #Para mirar los datos de las clases a través de un método en el admin de django
    def __str__(self):
        return self.documento, self.nombre, self.apellido, self.celular, self.correo

class Lineas_De_Credito(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    plazomax = models.IntegerField()
    montomax = models.IntegerField()

class Credito(models.Model):
    codigo_credito = models.IntegerField(primary_key=True)
    monto_prestado = models.IntegerField()
    fecha_credito = models.DateField() #Para fecha DateField
    #Llave foranea, documento del cliente
    documento = models.ForeignKey(Cliente, on_delete=models.CASCADE) #Si elimino un dato en la tabla credito, se elimna en la tabla cliente
    codigo = models.ForeignKey(Lineas_De_Credito, on_delete=models.CASCADE)

 

