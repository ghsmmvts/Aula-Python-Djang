from django.shortcuts import render

# Create your views here.

# def inicio(request):
#     return render(request, 'index.html')

# def comidas(request):
#     listaComidas = ['macarrao', 'acaraje', 'fondue', 'sushi']
    
#     parametros = {
#         'nome': 'comidas:',
#         'comidas': listaComidas
#     }

#     return render(request, 'comidas.html', parametros)

def inicio(request):
    return render(request, 'inicio.html')

def lista(request):
    lista = []

    parametros = {

    }

    return render(request, "arquivosdehtml", parametros)

def noticias(request):
    return render(request, 'noticias.html')
    