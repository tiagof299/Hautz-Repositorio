from django.shortcuts import render


def home(request):
    context = {
        'titulo': 'H A U T Z'
    }
    return render(request, 'index.html', context)
    
