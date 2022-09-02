from django.db import models

class Empleado(models.Model):
    identificacion = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    celular = models.CharField(max_length=15)
    correo = models.CharField(max_length=20)
    cargo = models.CharField(max_length=20)
    #Para mirar los datos de las clases a través de un método en el admin de django
    # def __str__(self):
     #   return self.documento, self.nombre, self.apellido, self.celular, self.correo

class Usuario(models.Model):
    identificacion = models.IntegerField(primary_key=True)
    clave = models.CharField(max_length=10)
    
class Empresa(models.Model):
    nit = models.IntegerField(primary_key=True) 
    identificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    actividad_economica = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=20)

class Ingresos_Gastos(models.Model):
    identificacion = models.IntegerField(primary_key=True)
    nit = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    ingresos = models.FloatField()
    gastos = models.FloatField()
