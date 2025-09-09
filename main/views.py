from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'StreetKicks',
        'your_name': 'Abelyvia Tori Rebecca Silalahi',
        'your_class': 'PBP F',
    }
    return render(request, 'main.html', context)