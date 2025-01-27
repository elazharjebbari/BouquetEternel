from django.shortcuts import render

# Create your views here.
def views_home(request):

    # Récupérer les sections avec les conférences ordonnées
    return render(request, 'handicrat/base.html')