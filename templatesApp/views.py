from django.shortcuts import render

# Create your views here.
def llamarTemplate(request):
    data = {
            "nombre" : "Juan",
            "apellido" : "Perez"
            }
    return render(request, 'templatesApp/vista1.html',data)


def infoUsuario(request):
    data = {
        "nombre" : "Peter Parker",
        "id" : "123",
        "correo" : "spiderman@clarin.cl"
    }
    return render(request, 'templatesApp/infoUsuario.html',data)