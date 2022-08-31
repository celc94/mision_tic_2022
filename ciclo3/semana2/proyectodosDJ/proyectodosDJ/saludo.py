from django.http import HttpResponse
def saludar(request, nombre, hora): #Este parámetro lo tiene por defecto, pero se pueden enviar datos por la URL
    return HttpResponse(f'Buenas Noches {nombre} {hora}')