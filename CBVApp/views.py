from django.shortcuts import render
from yaml import serialize
from sampleapp.serializer import UserSerializer
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateAPIView,
                                    ListAPIView,RetrieveDestroyAPIView)
from .models import Movie
from .serializer import MovieSerizlier
from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
# Create your views here.
class MovieListCreate(ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerizlier

class MovieRetriveUpdateView(RetrieveUpdateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerizlier
class MoviewListView(ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerizlier
class MoviewRetrievDestroy(RetrieveDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerizlier
    
###View Sets 

class MovieViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Movie.objects.all()
        serializer=MovieSerizlier(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset=Movie.objects.all()
        user=get_object_or_404(queryset,pk=pk)
        serializer=MovieSerizlier(user)
        return Response(serializer.data)

## Generic ViewSet 
class MoviewGeneric(viewsets.GenericViewSet):
    def get_queryset(self):
        queryset=Movie.objects.all()
        return queryset
    def get_object(self):
        queryset=self.get_queryset()
        obj=queryset.get(pk=self.kwargs['pk'])
        return obj
    def list(self,request):
        queryset=self.get_queryset()
        serializer=MovieSerizlier(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,**kwargs):
        obj=self.get_object()
        serializer=MovieSerizlier(obj)
        return Response(serializer.data)        
class MoviewModelSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerizlier