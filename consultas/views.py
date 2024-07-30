from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Estudiantes
from .serializer import EstudiantesSerializer
from tasks.models import Task
from tasks.serializer import TaskSerializer
# Create your views here.


class EstudiantesViewSet(viewsets.ViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer

    def list(self, request):
        serializer = EstudiantesSerializer(self.queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            estudiante = Estudiantes.objects.get(carnet=pk)
            id_estudiante = estudiante.id
            tasks = Task.objects.filter(foreign=id_estudiante)
            serializer_tareas = TaskSerializer(tasks, many=True)
            serializer_estudiante = EstudiantesSerializer(estudiante)
            return Response({'estudiante': serializer_estudiante.data, 'tareas': serializer_tareas.data}, status=200)
        except Estudiantes.DoesNotExist:
            return Response('Estudiante no encontrado', status=404)
        except Exception as e:
            return Response(str(e), status=500)
        # estudiante = Estudiantes.objects.get(carnet=pk)
        # serializer = EstudiantesSerializer(estudiante)
        # return Response(serializer.data)

    def create(self, request):
        serializer = EstudiantesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        estudiante = Estudiantes.objects.get(carnet=pk)
        serializer = EstudiantesSerializer(
            instance=estudiante, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        estudiante = Estudiantes.objects.get(carnet=pk)
        estudiante.delete()
        return Response('Estudiante eliminado')
