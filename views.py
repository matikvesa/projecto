from django.http import HttpResponse
from django.template import Template, context

def saludo(request):
    return HttpResponse("HOLA")

def probando(self):

    miHtml = open("C:\Users\Matias\Desktop\Proyecto Python\Django\Django\Plantilla\Prueba.html") 

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
    