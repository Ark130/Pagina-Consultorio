from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),
    path('pacientes', views.pacientes, name='pacientes'),
    path('pacientesview', views.pacientesview, name='pacientesview'),
    path('guardar_paciente', views.guardar_paciente, name='guardar_paciente'),
    path('eliminar_paciente', views.eliminar_paciente, name='eliminar_paciente'),
    path('actualizar_paciente', views.actualizar_paciente, name='actualizar_paciente'),
    path('citas', views.citas, name='citas'),
    path('citasview', views.citasview, name='citasview'),
    path('guardar_cita', views.guardar_cita, name='guardar_cita'),
    path('modificar_cita', views.modificar_cita, name='modificar_cita'),
    path('medico', views.medico, name='medico'),
    path('medicoview', views.medicoview, name='medicoview'),
    path('registrar_medico', views.registrar_medico, name='registrar_medico'),
    path('eliminar_medico', views.eliminar_medico, name='eliminar_medico'),
    path('eliminar_cita', views.eliminar_cita, name='eliminar_cita'),
    path('actualizar_medico', views.actualizar_medico, name='actualizar_medico'),
    path('historial', views.historial, name='historial'),
    path('registrar_historial', views.registrar_historial, name='registrar_historial'),
    
]
