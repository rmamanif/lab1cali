from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Candidato,Region

# Create your views here.

def index(request):
    latest_question_list = Region.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'elecciones/index.html', context)

def detalle(request, candidato_id):
    region = get_object_or_404(Region, pk=candidato_id)
    return render(request, 'elecciones/detalle.html' , {'region':region})

def votar(request, candidato_id):
    region = get_object_or_404(Region, pk=candidato_id)
    try: 
        selected_region = region.candidato_set.get(pk=request.POST['candidato'])
    except(KeyError, Region.DoesNotExist):
        return render(request, 'elecciones/detalle.html', {
        'region':region,
        'error_message':'No has seleccionado un candidato.',
        })
    else:
        selected_region.votos +=1
        selected_region.save()
    return HttpResponseRedirect(reverse('elecciones:detalle',args=(candidato_id,)))

def resultados(request, candidato_id):
    region = get_object_or_404(Region, pk=candidato_id)
    return render(request, 'elecciones/resultados.html', {'region':region})

