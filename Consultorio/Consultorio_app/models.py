from django.db import models

# Tabla Paciente
class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    nombreCompleto = models.CharField(max_length=255)
    edad = models.IntegerField()
    fechaNac = models.DateField()
    historialMedico = models.OneToOneField('HistorialMedico', on_delete=models.CASCADE, related_name='paciente')

    def agendarCita(self, medico, fecha):
        # Lógica para agendar cita
        pass

    def cancelarCita(self, medico, fecha):
        # Lógica para cancelar cita
        pass

    def modificarCita(self, medico, fecha):
        # Lógica para modificar cita
        pass

    def proporcionarInformacion(self):
        # Retorna el historial médico
        return self.historialMedico

    def __str__(self):
        return f"Paciente {self.nombreCompleto}"


# Tabla Medico
class Medico(models.Model):
    idMedico = models.AutoField(primary_key=True)
    nombreCompleto = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    citas = models.ManyToManyField('Cita', related_name='medicos')
    recetas = models.ManyToManyField('Receta', related_name='recetas_medico')

    def atenderConsulta(self, paciente, consulta):
        # Lógica para atender consulta
        pass

    def tratamiento(self, consulta):
        # Lógica para prescribir tratamiento
        return consulta.tratamiento

    def verificarHistorialMedico(self, paciente):
        return paciente.proporcionarInformacion()

    def __str__(self):
        return f"Medico {self.nombreCompleto} - Especialidad: {self.especialidad}"


# Tabla Cita
class Cita(models.Model):
    fecha = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='citas_medico')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas_paciente')

    def crearCita(self, medico, paciente, fecha):
        # Lógica para crear cita
        pass

    def modificarCita(self, fecha):
        # Lógica para modificar cita
        self.fecha = fecha

    def cancelarCita(self):
        # Lógica para cancelar cita
        pass

    def __str__(self):
        return f"Cita del {self.paciente} con {self.medico} el {self.fecha}"


# Tabla Tratamiento
class Tratamiento(models.Model):
    descripcion = models.TextField()
    duracion = models.IntegerField()  # En días
    medicamentos = models.ManyToManyField('Medicamento')

    def crearTratamiento(self, descripcion, duracion):
        self.descripcion = descripcion
        self.duracion = duracion

    def monitorearTratamiento(self):
        # Lógica para monitorear el tratamiento
        pass

    def __str__(self):
        return f"Tratamiento: {self.descripcion} - Duración: {self.duracion} días"


# Tabla Receta
class Receta(models.Model):
    medicamentos = models.ManyToManyField('Medicamento')
    indicaciones = models.TextField()

    def emitirReceta(self, diagnostico):
        # Lógica para emitir receta
        pass

    def __str__(self):
        return f"Receta con indicaciones: {self.indicaciones}"


# Tabla Recepción
class Recepcion(models.Model):
    nombre = models.CharField(max_length=255)
    pacientes = models.ManyToManyField(Paciente, related_name='recepcion_pacientes')
    citas = models.ManyToManyField(Cita, related_name='recepcion_citas')
    mediosDeContacto = models.JSONField()

    def agregarPaciente(self, paciente):
        # Lógica para agregar paciente
        pass

    def modificarPaciente(self, paciente):
        # Lógica para modificar paciente
        pass

    def gestionarCitas(self):
        # Lógica para gestionar citas
        pass

    def informacionPaciente(self):
        # Lógica para retornar información del paciente
        return self.pacientes

    def __str__(self):
        return f"Recepción {self.nombre}"


# Tabla Historial Medico
class HistorialMedico(models.Model):
    antecedentes = models.TextField()
    diagnosticos = models.ManyToManyField('Diagnostico')
    tratamientos = models.ManyToManyField(Tratamiento)
    alergias = models.CharField(max_length=255)
    notas = models.TextField()

    def registrarAntecedentes(self, antecedentes):
        # Lógica para registrar antecedentes
        self.antecedentes = antecedentes

    def registrarDiagnosticos(self, diagnostico):
        # Lógica para registrar diagnósticos
        self.diagnosticos.add(diagnostico)

    def registrarTratamientos(self, tratamiento):
        # Lógica para registrar tratamientos
        self.tratamientos.add(tratamiento)

    def agregarNotas(self, notas):
        # Lógica para agregar notas
        self.notas = notas

    def __str__(self):
        return f"Historial Médico de Paciente"


# Tabla Diagnóstico
class Diagnostico(models.Model):
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion


# Tabla Medicamento
class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre