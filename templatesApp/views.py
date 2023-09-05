from django.shortcuts import render

# Create your views here.
def llamarTemplate(request):
    return render(request, 'templatesApp/vista1.html')