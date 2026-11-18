from django.db import models
from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cli = models.CharField(max_length=100)
    email_cliente = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cli}"


class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nombre_tecnico = models.CharField(max_length=100)
    apellido_tec = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_tecnico} {self.apellido_tec}"


class Zona(models.Model):
    id_zona = models.AutoField(primary_key=True)
    zona = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.zona


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, unique=True, default='ingresado')

    def __str__(self):
        return self.estado


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    numero_serie = models.CharField(max_length=100, unique=True)
    id_anam = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id_anam} "




class OrdenTrabajo(models.Model):
    ot = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_zona = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    observacion = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    materiales = models.TextField(blank=True)
    info_retiro = models.TextField(blank=True)
    fecha_ingreso = models.DateField()
    fecha_termino = models.DateField(null=True, blank=True)
    fecha_retiro = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"OT-{self.ot} ({self.id_cliente})"

class Bateria(models.Model):
    id_bateria = models.AutoField(primary_key=True)
    num_bateria = models.CharField(max_length=100, unique=True)  
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.num_bateria} "

class CambioBateria(models.Model):
    ot_bateria = models.AutoField(primary_key=True)
    num_bateria = models.ForeignKey(Bateria, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_zona = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True)    
    info_retiro = models.TextField(blank=True)   
    fecha_solicitud_bateria = models.DateField()
    fecha_retiro_bateria = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Cambio Batería {self.num_bateria}  Cliente: {self.id_cliente}"