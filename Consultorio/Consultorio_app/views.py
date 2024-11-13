from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from .models import Paciente, Cita, Medico, HistorialMedico, Tratamiento, Diagnostico


# Create your views here.

def inicio (request):
    return render(request, 'Paginas/inicio.html')

def citas (request):
    return render(request, 'Paginas/citas.html')

def medico (request):
    return render(request, 'Paginas/medico.html')

def historial (request):
    return render(request, 'Paginas/historial.html')

def medicoview (request):
    return render(request, 'Paginas/medicoview.html')

# Vista para mostrar la lista de pacientes
def pacientesview(request):
    pacientes = Paciente.objects.all()
    return render(request, 'Paginas/pacientesview.html', {'pacientes': pacientes})

def citasview (request):
    return render(request, 'Paginas/citasview.html')

@csrf_protect
def pacientes (request):
    return render(request, 'Paginas/pacientes.html')

def registrar_historial(request):
    if request.method == 'POST':
        antecedentes = request.POST['antecedentes']
        diagnosticos = request.POST.getlist('diagnosticos')
        tratamientos = request.POST.getlist('tratamientos')
        alergias = request.POST['alergias']
        notas = request.POST['notas']

        historial = HistorialMedico(
            antecedentes=antecedentes,
            alergias=alergias,
            notas=notas
        )
        historial.save()
        for diagnostico_id in diagnosticos:
            diagnostico = Diagnostico.objects.get(id=diagnostico_id)
            historial.diagnosticos.add(diagnostico)
        for tratamiento_id in tratamientos:
            tratamiento = Tratamiento.objects.get(id=tratamiento_id)
            historial.tratamientos.add(tratamiento)
        historial.save()

        return redirect('some_success_url')

    diagnosticos = Diagnostico.objects.all()
    tratamientos = Tratamiento.objects.all()
    return render(request, 'historial.html', {'diagnosticos': diagnosticos, 'tratamientos': tratamientos})



@csrf_protect
def guardar_paciente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        historial_medico = request.POST['historial_medico']
        # Aquí puedes guardar los datos en la base de datos
        # ...
        return redirect('pacientes')
    return render(request, 'pacientes.html')


@csrf_protect
def eliminar_paciente(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('selectedPaciente')
        paciente = get_object_or_404(Paciente, id=paciente_id)
        paciente.delete()
        return redirect('pacientesview')  # Cambia a tu vista de lista de pacientes
    return redirect('pacientesview')

@csrf_protect
def actualizar_paciente(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('pacienteId')
        paciente = get_object_or_404(Paciente, id=paciente_id)
        
        # Actualizar los campos del paciente
        paciente.nombre = request.POST['nombre']
        paciente.edad = request.POST['edad']
        paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
        paciente.historial_medico = request.POST['historial_medico']
        paciente.save()
        
        return redirect('pacientesview')  # Cambia a tu vista de lista de pacientes
    return redirect('pacientesview')


def eliminar_cita(request):
    if request.method == 'POST':
        cita_id = request.POST.get('selectedCita')
        if cita_id:
            cita = get_object_or_404(Cita, id=cita_id)
            cita.delete()
            messages.success(request, "Cita eliminada exitosamente.")
        else:
            messages.error(request, "No se seleccionó ninguna cita para eliminar.")
    return redirect('lista_citas')  # Asegúrate de tener una URL llamada 'lista_citas' para redireccionar


@csrf_protect
def guardar_cita(request):
    if request.method == 'POST':
        fecha_hora = request.POST.get('fecha_hora')
        medico = request.POST.get('medico')
        paciente = request.POST.get('paciente')

        # Crea y guarda la nueva cita en la base de datos
        nueva_cita = Cita(fecha_hora=fecha_hora, medico_id=medico, paciente_id=paciente)
        nueva_cita.save()

        return redirect('citas')  # Cambia 'citas' al nombre de la página que prefieras

    return render(request, 'citas.html')  # Renderiza el formulario si no es POST

@csrf_protect
def registrar_medico(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        especialidad = request.POST['especialidad']
        telefono = request.POST['telefono']
        email = request.POST['email']

        # Crea y guarda el nuevo médico en la base de datos
        nuevo_medico = Medico(nombre=nombre, especialidad=especialidad, telefono=telefono, email=email)
        nuevo_medico.save()

        return redirect('medicos')  # Cambia 'medicos' al nombre de la página que prefieras

    return render(request, 'medico.html')


def eliminar_medico(request):
    if request.method == 'POST':
        medico_id = request.POST.get('selectedMedico')
        medico = get_object_or_404(Medico, id=medico_id)
        medico.delete()
        return redirect('medicoview')  # Cambia 'medicoview' al nombre de tu vista de lista de médicos


from django.shortcuts import redirect, get_object_or_404
from .models import Medico

def actualizar_medico(request):
    if request.method == 'POST':
        medico_id = request.POST.get('medicoId')
        medico = get_object_or_404(Medico, id=medico_id)
        medico.nombre = request.POST.get('nombre')
        medico.especialidad = request.POST.get('especialidad')
        medico.telefono = request.POST.get('telefono')
        medico.email = request.POST.get('email')
        medico.save()
        return redirect('medicoview')  # Cambia 'medicoview' al nombre de tu vista de lista de médicos



@csrf_protect
def modificar_cita(request):
    if request.method == 'POST':
        cita_id = request.POST.get('cita_id')
        fecha_hora = request.POST.get('fecha_hora')
        medico_id = request.POST.get('medico')
        paciente_id = request.POST.get('paciente')

        # Obtén la cita existente y actualiza sus campos
        cita = get_object_or_404(Cita, id=cita_id)
        cita.fecha_hora = fecha_hora
        cita.medico_id = medico_id
        cita.paciente_id = paciente_id
        cita.save()

        return redirect('citas')  # Cambia 'citas' al nombre de la página que prefieras

    return redirect('citas')  # Redirige a la página de citas si no es POST