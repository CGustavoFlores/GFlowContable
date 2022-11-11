from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import Http404
from Contable.models import ContaCapitulos
from .forms import CapituloForm
from django.http import HttpResponseRedirect



# Create your views here.

# function to render to frontpage
def frontend(request):
    return render(request,"frontend.html")


# el home , que es la pagina inicial , va a pedir un login 
def home(request):
    return render(request, "home.html")


# ---- views del backend 

@ cache_control(no_cache=True, must_revalidate=True, no_store=True)
@ login_required(login_url='login')
def backend(request):
    return render (request, "backend.html")


@login_required( login_url="/Login" )
def capitulos(request):
    capitulos = ContaCapitulos.objects.all()
    page= request.GET.get('page',1)
    try:
        paginator = Paginator(capitulos, 30) 
        capitulos=paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': capitulos,
        'paginator': paginator
    }
    return render(request, 'Tablas/Capitulos.html', data)



def nuevo_capitulo(request):
    data = {
        'form': CapituloForm()
    }
    if request.method == 'POST':
        formulario=CapituloForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Registrado OK !! "
            messages.success(request,"Registrado OK !!!")
            #return HttpResponseRedirect('Tablas/Capitulos/')
            return redirect(to='capitulos')
        else:
            data["form"]=formulario

    return render(request, 'Tablas/capitulo_add.html',data)

#-----------------------------------
# esta es otra forma , segun mastery
# ---------------------------------- 
#def alta_capitulo(request):
#    data=CapituloForm(request.POST or None)
#    if data.is_valid():
#        data.save()
#        messages.success(request, "Registrado Ok!!")
#        return HttpResponseRedirect('/')
#    context = {
#        "form":data
#    }
#    return render(request, 'Tablas/capitulo_add.html',context)




# function to insert new capitulo
#@cache_control(no_cache=True,must_revalidade=True, no_store=True)
#@login_required(login_url='login')
#def alta_capitulo(request):
#    if request.method == "POST":
#        if request.POST.get('IdCapitulo') and request.POST.get('IdCapitulo') and request.POST.get('Denominacion'):
#            capitulo=ContaCapitulos()          
#            capitulo.IdCapitulo =request.POST.get('IdCapitulo')
#            capitulo.Denominacion =request.POST.get('Denominacion')
#            capitulo.save()
#            messages.success(request,"Se agrego un capitulo contable !")
#            return HttpResponseRedirect('/Capitulos')
#    else:
#        return render(request, 'capitulo_add.html')






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

