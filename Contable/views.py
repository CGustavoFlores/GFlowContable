from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def capitulos(request):
    return render(request, "Tablas/Capitulos")

def ctas_madres(request):
    return render(request, "Tablas/Ctas_Madres.html")

def cuentas(request):
    return render(request, "Tablas/Cuentas.html")

def plan_cuenta(request):
    return render(request, "Tablas/Plan_Cuenta.html")

def rubros(request):
    return render(request, "Tablas/Rubros.html")




def crud_ejercicio(request):
    return render(request, "Contabilidad/Crud_Ejercicio.html")


def apertura_ejercicio(request):
    return render(request, "Contabilidad/Apertura_Ejercicio.html")

def Asientos(request):
    return render(request, "Contabilidad/Asientos.html")

def Cierre_Patrimonial(request):
    return render(request, "Contabilidad/Cierre_Patrimonial")

def Cierre_Resultado(request):
    return render(request, "Contabilidad/Cierre_Resultado")

def Cierre_Ejercicio(request):
    return render(request, "Contabilidad/Cierre_Ejercicio")

def GenerarSys(request):
    return render(request,"Contabilidad/GenerarSys.html")

