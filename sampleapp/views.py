import email
import profile
from django.forms import PasswordInput
from django.shortcuts import render
from rest_framework import serializers
from sampleapp.serializer import BookSerializer,RegisterSerializer,UserSerializer,LoginSerializer,ChangePasswordSerializer
from sampleapp.models import Book,B2CUser
from rest_framework.decorators import api_view,parser_classes,permission_classes
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework import status
from django.contrib.auth import authenticate
from .service import generatetoken
from rest_framework.parsers import MultiPartParser,FormParser
# Create your views here.
import pandas as pd
import json
from pandas.io.json import json_normalize


@api_view(['POST'])
@permission_classes([AllowAny])
def BookView(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def Register(request):
    print(request.data)
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllUsers(request):
    data=B2CUser.objects.all()
    serializer=UserSerializer(data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SingleUser(request,pk):
    singledata=B2CUser.objects.get(id=pk)
    serializer=UserSerializer(singledata)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Updateuserdata(request,pk):
    userdata=B2CUser.objects.get(id=pk)
    serializer=UserSerializer(instance=userdata,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

    
     
@api_view(['POST'])
@permission_classes([AllowAny])
def Login(request):
    serializer=LoginSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("serializer block")
        #we are querying to get the single  row data
        user=B2CUser.objects.get(email=serializer.data["email"]) 
        user_auth=authenticate(email=user.email,password=serializer.data["password"])
        token=generatetoken(user)
        print(token)
        return Response(token,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser])
def FileConversion(request):
    print(request.FILES)
    file_list=request.FILES.getlist('file')
    # for item in file_list:
        # with open(item) as json_file:
        #     newdata=json.load(json_file)
        #     print(newdata)
        #     data=json.loads(newdata[0])
        #     print(data)
        # mydata=data["analysis"]
    
    with open(request.FILES['file']) as json_file:
        newdata=json.load(json_file)
        data=json.loads(newdata[0])
    mydata=data["analysis"]
   
    df=pd.json_normalize(mydata,'timeseries','company_name')
    df1=pd.json_normalize(mydata,'networks','company_name')



    results=pd.merge(df,df1,on='company_name')
    results.to_csv('MYFineTest.csv',index=False)
    


@api_view(['POST'])
@permission_classes([AllowAny])
def Change_Password(request):
    serializer=ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        user=B2CUser.objects.get(email=serializer.data["email"])
        user.set_password(serializer.data["newpassword"])
        user.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
# email
# PasswordInput
# front end framework---html--email,password--submit--loginapi--op--token-
# ff--token--decode the token--
# my profile
# all userdata-- all users button--cookie service--token--button--token,alluser--will get the data  
        
            
        
        
        
    
    
    # 1: we have given credential---token
    # 2.to fethc is authenticated api---to pass tthe credential
    
    # token---with api---it will give u the results:
        
   