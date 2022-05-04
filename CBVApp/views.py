from django.shortcuts import render
from yaml import serialize
from sampleapp.serializer import UserSerializer
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateAPIView,
                                    ListAPIView,RetrieveDestroyAPIView)
from .models import Movie
from .serializer import MovieSerizlier


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
    


    