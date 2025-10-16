from django.urls import path

from . import views #importa nossas views

urlpatterns = [
          path('',views.listar_projetos, name = 'listar_projetos'),        
]