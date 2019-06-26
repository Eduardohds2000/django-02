from django.shortcuts import render

# Create your views here.

def  mostrar_index(request):
    return render (request, 'index.html')

def mostrar_pombos(request):
    return render (request, 'pombos.html')

def mostrar_rolezinho(request):
    roles = ['bailao','shopping união', 'Quermesse da Paróquia de Sao Joao', 'Calçadão de Osasco', 'SESC', 'Risca Faca']
    bairro = 'Rochdale',
    return render (request, 'rolezinho.html', {'roles': roles, 'bairro': bairro} )