from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
# Create your models here.

class Tipo_Usuario(models.Model):
    descripcion = models.CharField(max_length=25,null=False)

    def __str__(self):
        return 'TIPO_USUARIO'

class Rol_Usuario(models.Model):
    nombre_rol = models.CharField(max_length=25,null=False)

    def __str__(self):
        return 'ROL_USUARIO'

class Descuento(models.Model):
    porcentaje = models.IntegerField(null=False)

    def __str__(self):
        return 'Descuento'


class Convenio_Usuario(models.Model):
    organizacion = models.CharField(max_length=25,null=False)
    descuento = models.ForeignKey(Descuento,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return 'CONVENIO_USUARIO'





class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=14, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=False)
    telefono =  models.CharField(max_length=50, null=False)
    tipo_usuario = models.ForeignKey(Tipo_Usuario,on_delete=models.CASCADE, blank=True, null=True)
    rol_usuario = models.ForeignKey(Rol_Usuario,on_delete=models.CASCADE,null=True)
    convenio_usuario = models.ForeignKey(Convenio_Usuario,on_delete=models.CASCADE,null=True)
    credenciales  = models.OneToOneField(User,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return 'USUARIO'

    class Meta:

        permissions = (
            ('is_administrador',_('is administrador')),
            ('is_tecnico',_('is tecnico')),
            ('is_cliente',_('is cliente')),
        )

        


        

    

class Invitacion(models.Model):
    email = models.EmailField(null=False)
    descripcion = models.CharField(max_length=50,null=False)
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return 'INVITACION'


class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=25,null=False)
    encargadorut = models.CharField(max_length=14,null=False)
    usuario = models.ManyToManyField(Usuario)

    def __str__(self):
        return 'CONVENIO_USUARIO'

class Seguimiento(models.Model):
    descripcion = models.CharField(max_length=25,null=False)

    def __str__(self):
        return 'EQUIPO'

class Sub_servicio(models.Model):
    descripcion = models.CharField(max_length=100,null=False)
    precio = models.IntegerField(null=False)

    def __str__(self):
        return 'TIPO_SERVICIO'


class Tipo_servicio(models.Model):
    descripcion = models.CharField(max_length=100,null=False)
    sub_servicio = models.ForeignKey(Sub_servicio,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return 'TIPO_SERVICIO'

class Servicio(models.Model):
    nombre = models.CharField(max_length=25,null=False)
    descripcion = models.CharField(max_length=100,null=False)
    tipo_servicio = models.ForeignKey(Tipo_servicio,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return 'SERVICIO'


class Solicitud(models.Model):
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, blank=True, null=True)
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE,null=True)
    seguimiento = models.ForeignKey(Seguimiento,on_delete=models.CASCADE,null=True)
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return 'SOLICITUD'

class Solicitud_historial(models.Model):
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    descripcion = models.CharField(max_length=200,null=False)
    solicitud = models.ForeignKey(Solicitud,on_delete=models.CASCADE,null=True)
    seguimiento = models.ForeignKey(Seguimiento,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return 'SOLICITUD_HISTORIAL'

 

##DIRECCIONES 
class Region(models.Model):
    name = models.CharField(max_length = 30,null = False)

class Ciudad(models.Model):
    name = models.CharField(max_length = 30,null = False)
    region = models.ForeignKey(Region, on_delete = models.CASCADE, null = False)

class Comuna(models.Model):
    name = models.CharField(max_length = 30,null = False)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE, null = False)
    def str(self):
        return self.name


