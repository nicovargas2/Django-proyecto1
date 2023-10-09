from django.http import HttpResponse
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola Django!")


def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre):
    documentoDeTexto = f"""<div style="text-align:center;">
    <h1 style="color: blue">Bienvenido:<h1> 
    <h3> {nombre} </h3> 
    </div>"""
    # documentoDeTexto = f"Bienvenido: <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)
