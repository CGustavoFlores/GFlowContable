from django.urls import path
from .views import home, capitulos,rubros,ctas_madres,cuentas,plan_cuenta, apertura_ejercicio,Asientos, Cierre_Resultado, Cierre_Patrimonial,Cierre_Ejercicio,GenerarSys


urlpatterns = [
    path("", home,name="home"),
    path("Tablas/Capitulos/", capitulos,name="capitulos"),
    path("Tablas/Rubros/", rubros ,name="rubros"),
    path("Tablas/Ctas_Madres/", ctas_madres ,name="ctasmadres"),
    path("Tablas/Cuentas/",cuentas ,name="cuentas"),
    path("Tablas/Plan_Cuenta/", plan_cuenta ,name="plancuenta"),


]
