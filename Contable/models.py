from django.db import models


# Create your models here.


class ContaCapitulos(models.Model):
    IdCapitulo = models.CharField(max_length=1, primary_key=True)
    Denominacion = models.CharField(max_length=30 )
    
    def __str__(self):
        return self.Denominacion

    class Meta:
        db_table = 'ContaCapitulo'


class ContaRubros(models.Model):
    IdRubro = models.CharField(max_length=3, primary_key=True)
    IdCapitulo = models.ForeignKey(ContaCapitulos, on_delete= models.SET_NULL, null=True)
    Denominacion = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'ContaRubros'
        unique_together = (('IdRubro', 'IdCapitulo'),)

class ContaCtaMadre(models.Model):
    IdCtaMadre = models.CharField(max_length=6, primary_key=True)
    IdRubro = models.ForeignKey(ContaRubros, on_delete= models.SET_NULL, null=True)
    Denominacion = models.CharField(max_length=50,default='')
    
    class Meta:
        db_table = 'ContaCtaMadre'
      
class ContaCuentas(models.Model):
    IdCuenta = models.CharField(max_length=12, primary_key=True)
    IdCtaMadre = models.ForeignKey(ContaCtaMadre, on_delete= models.SET_NULL, null=True)
    IdCtaAuxiliar = models.CharField(max_length=9, default='')
    Denominacion = models.CharField(max_length=80,default='')
    Movimiento = models.BooleanField(default=True) 
    Saldo = models.CharField(max_length=1, default='')
    Clasificacion = models.CharField(max_length=1, default='')
    CodigoCorto= models.IntegerField(default=0)
    SubCuenta= models.BooleanField(default=False)
    
    class Meta:
        db_table = 'ContaCuentas'
