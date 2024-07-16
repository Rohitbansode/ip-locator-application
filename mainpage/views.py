from django.shortcuts import render

# Create your views here.

import requests

def ip_locator(request):
    ip_address = request.GET.get('ip', '')
    if ip_address:
        url = f'http://ip-api.com/json/{ip_address}'
        response = requests.get(url)
        data = response.json()
        return render(request, 'ip-finder.html', {'data': data})
    return render(request, 'ip-finder.html')
