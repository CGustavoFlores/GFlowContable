
from django.contrib import admin
from django.urls import path, include
from Contable import views
from .views import home, capitulos,rubros,ctas_madres,cuentas,plan_cuenta, apertura_ejercicio,Asientos, Cierre_Resultado, Cierre_Patrimonial,Cierre_Ejercicio,GenerarSys


urlpatterns = [

     # Native path to access then django admin
    path('admin/', admin.site.urls),
    
    # path to access to frontend page
    path('', views.frontend, name="frontend"),
    
    # path to login/logout
    path('login', include('django.contrib.auth.urls')),

    #-------------  BACKEND SECTION------------------#
    # path to access to backend page
    path('backend/', views.backend, name="backend"),

    path("Tablas/Capitulos/", views.capitulos,name="capitulos"),
    path("Tablas/capitulo_add/", views.nuevo_capitulo,name="alta_capitulo"),

    path("Tablas/Rubros/", rubros ,name="rubros"),
    path("Tablas/Ctas_Madres/", ctas_madres ,name="ctasmadres"),
    path("Tablas/Cuentas/",cuentas ,name="cuentas"),
    path("Tablas/Plan_Cuenta/", plan_cuenta ,name="plancuenta"),


]
