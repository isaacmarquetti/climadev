import json

from django.shortcuts import render
import requests


def home(request):
    return render(request, 'previsao/home.html')


def busca(request):
    cidade = request.GET.get('cidade')
    api_key = "93f5ba284dd0564a92844a257348fa5f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang=pt_br&appid={api_key}&units=metric"
    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={cidade}&limit=5&appid={api_key}"

    resposta = requests.get(url).json()
    resposta_city = requests.get(url_city).json()

    nome = resposta_city[0]['name']
    state = resposta_city[0]['state']
    temp = resposta['main']['temp']
    pais = resposta['sys']['country']
    temp_max = resposta['main']['temp_max']
    temp_min = resposta['main']['temp_min']
    sensacao = resposta['main']['feels_like']
    condicao = resposta['weather'][0]['description']
    icon = resposta['weather'][0]['icon']
    foto = f'http://openweathermap.org/img/wn/{icon}@2x.png'

    return render(request, 'previsao/home.html', {
        'nome': nome,
        'estado': state,
        'local': f'{cidade}, {pais}',
        'cidade': f'{cidade}',
        'temp': f'{temp:.0f} ºC',
        'temp_max': f'{temp_max:.0f} ºC',
        'temp_min': f'{temp_min:.0f} ºC',
        'sensacao': f'{sensacao:.0f} ºC',
        'condicao': f'{(condicao.title())}',
        'icon': foto,

    })


def listar_cidades(request):
    cidade = request.GET.get('cidade')
    api_key = "93f5ba284dd0564a92844a257348fa5f"

    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={cidade}&limit=5&appid={api_key}"
    print(url_city)

    resposta_city = requests.get(url_city).json()
    print(resposta_city)




