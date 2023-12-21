from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import InscritoForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InstitucionForm  
from .models import Institucion
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from .forms import InscritoForm



class IndexView(View):
    def get(self, request):
        return render(request, 'index.html') 
    
class ListaInstituciones(APIView):
    def get(self, request):
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListaInscritos(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InscripcionPersonaView(View):
    def get(self, request):
        form = InscritoForm() 
        return render(request, 'inscripcion_persona.html', {'form': form})

    def post(self, request):
        form = InscritoForm(request.POST)  
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))  
        return render(request, 'inscripcion_persona.html', {'form': form})
    
def inscripcion_institucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = InstitucionForm()  
    
    return render(request, 'inscripcion_institucion.html', {'form': form})


class DetalleInscrito(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(pk=pk)
        except Inscrito.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        inscrito = self.get_object(pk)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    def put(self, request, pk):
        inscrito = self.get_object(pk)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscrito = self.get_object(pk)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DetalleInstitucion(APIView):
    def get_object(self, pk):
        try:
            return Institucion.objects.get(pk=pk)
        except Institucion.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        institucion = self.get_object(pk)
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)

    def put(self, request, pk):
        institucion = self.get_object(pk)
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def lista_inscritos(request):
    if request.method == 'GET':
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class AlumnoAPIView(APIView):
    def get(self, request):
        alumno = {
            "nombre": "Natalia Lienqueo Tworowski",
            "edad": 21,
            "universidad": "INACAP",
            "carrera": "Ingeniería Informática",
            "seccion": "IEI170",
        }
        return Response(alumno)
