from django.urls import path

from . import views

app_name ='elecciones'

urlpatterns = [

    #ex: /encuesta/
    path('', views.index, name='index'),
    #ex: /elecciones/1/
    path('<int:candidato_id>/', views.detalle, name='detalle'),
    #ex: /elecciones/5/resultados/
    path('<int:candidato_id>/resultados/', views.resultados, name='resultados'),
    #ex: /elecciones/5/voto/ 
    path('<int:candidato_id>/voto/',views.votar, name="votar"),
]