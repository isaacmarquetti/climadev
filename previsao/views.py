from django.shortcuts import render
import requests


def home(request):
    return render(request, 'previsao/home.html')


def busca(request):
    cidade = request.GET.get('cidade')
    api_key = "93f5ba284dd0564a92844a257348fa5f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang=pt_br&appid={api_key}&units=metric"

    resposta = requests.get(url).json()

    temp = resposta['main']['temp']
    pais = resposta['sys']['country']
    temp_max = resposta['main']['temp_max']
    temp_min = resposta['main']['temp_min']
    sensacao = resposta['main']['feels_like']
    condicao = resposta['weather'][0]['description']
    icon = resposta['weather'][0]['icon']
    foto = f'http://openweathermap.org/img/wn/{icon}@2x.png'

    return render(request, 'previsao/home.html', {
        'local': f'{cidade}, {pais}',
        'cidade': f'{cidade}',
        'temp': f'{temp:.0f} ºC',
        'temp_max': f'{temp_max:.0f} ºC',
        'temp_min': f'{temp_min:.0f} ºC',
        'sensacao': f'{sensacao:.0f} ºC',
        'condicao': f'{(condicao.title())}',
        'icon': foto,

    })



