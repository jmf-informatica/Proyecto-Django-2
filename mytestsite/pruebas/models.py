from django.db import models

# Create your models here.

class Periodos(models.Model):
    periodo=models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.periodo)
    
    class Meta():
        verbose_name_plural='Periodos'

class Paises(models.Model):
    pais=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.pais)

    class Meta():
        verbose_name_plural='paises'


class Productos(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=300)
    periodo=models.ForeignKey(Periodos, on_delete=models.CASCADE,blank=True,null=True)
    pais=models.ForeignKey(Paises, on_delete=models.CASCADE,blank=True,null=True)
    PrecioCompra=models.FloatField(null=True, blank=True)
    PrecioRenovacion=models.FloatField(null=True, blank=True)

    def __str__(self):
        return '{}{}{}{}{}'.format(self.nombre,self.periodo,self.pais,self.PrecioCompra,self.PrecioRenovacion)

    class Meta():
        verbose_name_plural='Productos'
