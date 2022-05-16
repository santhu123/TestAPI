"""NewProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from sampleapp import views as vw
#from CBVApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('createbookdata/',views.BookView),
    path('signup',vw.Register),
    path('users',vw.AllUsers),
    path('login',vw.Login),
    # path('single/<str:pk>',views.SingleUser),
    # path('updateuser/<str:pk>',views.Updateuserdata),
    # path('fileconvert',views.FileConversion),
    
    # path('changepassword',views.Change_Password),
    # path('addmovie',views.MovieListCreate.as_view()),
    # path('movielist',views.MoviewListView.as_view()),
    # path('updatemoview/<int:pk>',views.MovieRetriveUpdateView.as_view()),
    # path('deletemovie/<int:pk>',views.MoviewRetrievDestroy.as_view()),
=======
from sampleapp import  views
#from CBVApp import views
from rest_framework.routers import DefaultRouter

# router=DefaultRouter()
# router.register('movie-example',views.MovieViewset,basename='moview')
# router.register('moviegen-example',views.MoviewGeneric,basename='moviegen')
# router.register('moviemodel-example',views.MoviewModelSet,basename='moviemodel')

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('createbookdata/',views.BookView),
    path('signup',views.Register),
    path('users',views.AllUsers),
    path('login',views.Login),
    path('single/<str:pk>',views.SingleUser),
    path('updateuser/<str:pk>',views.Updateuserdata),
    # path('fileconvert',views.FileConversion),
    
    # # path('changepassword',views.Change_Password),
    # path('addmovie',views.MovieListCreate.as_view()),
    # path('movielist',views.MoviewListView.as_view()),
    # path('updatemoview/<int:pk>',views.MovieRetriveUpdateView.as_view()),
    #  path('deletemovie/<int:pk>',views.MoviewRetrievDestroy.as_view()),
>>>>>>> d80158ac213e687e5c8e1304cdb1dd9cedaabf0c
 
    
]
#urlpatterns.router
# http://127.0.0.1:800/singup

# function--send the data--will be sent to http://127.0.0.1:800/singup via HTTP Request ..

# the data will be sent in body of the request
# # Django---

# username --this won't be in ur control 
# password  


