"""
URL configuration for LIENQUEO_NATALIA_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from LIENQUEO_NATALIA_FINAL_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('inscritos/', views.ListaInscritos.as_view(), name='lista_inscritos'),
    path('inscritos/<int:pk>/', views.DetalleInscrito.as_view(), name='detalle_inscrito'),
    path('instituciones/', views.ListaInstituciones.as_view(), name='lista_instituciones'),
    path('instituciones/<int:pk>/', views.DetalleInstitucion.as_view(), name='detalle_institucion'),
    path('alumno_api/', views.AlumnoAPIView.as_view(), name='alumno_api'),
    path('inscripcion_persona/', views.InscripcionPersonaView.as_view(), name='inscripcion_persona'),
    path('inscripcion_institucion/', views.inscripcion_institucion, name='inscripcion_institucion'),
]


