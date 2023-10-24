from django.shortcuts import render
from django.http import HttpResponse
from .models import Entidad,Comunicado




# Create your views here.
def index(request):
    #aqui va el titulo
    cantidad_comunicados=Comunicado.objects.count()
    id_entidad= request.GET.get('id_entidad')
    if id_entidad:
        comunicado=Comunicado.objects.filter(entidad=id_entidad).order_by('-fecha_publicacion')
    else:
        comunicado=Comunicado.objects.all().order_by('-fecha_publicacion')
    entidades =Entidad.objects.all()

    data ={

        "Comunicado":comunicado,
        "Entidad":entidades,

    }

    return render(request,"myapp/index.html",data)
