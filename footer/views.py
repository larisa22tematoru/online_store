from django.shortcuts import render


def politica_de_retur(request):
    return render(request, 'footer/politica_de_retur.html')

def touch_of_gold_club(request):
    return render(request, 'footer/touch_of_gold_club.html')

def responsabilitate(request):
    return render(request, 'footer/responsabilitate.html')

def setari_cookieuri(request):
    return render(request, 'footer/setari_cookieuri.html')
