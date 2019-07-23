from django.shortcuts import render

# Create your views here.

def funcao (request):
    return render(request, "base.html")

def noticias(request):
    listaNoticias = ['Governo', 'Economia', 'Tempo']

    parametros = {
        'nome': 'noticias:',
        'noticias': listaNoticias
   }

    return render(request, 'noticias.html', parametros)



    