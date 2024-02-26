from django.shortcuts import render
from django.http import JsonResponse
from .models import Candidate , Category, Event
from .serializers import CandidateSerializer , CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def all_candidate(request):

    if request.method =='GET':

        candidates =Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many = True)
        return JsonResponse(serializer.data, safe=False)


    if request.method =='POST':
        serializer = CandidateSerializer (data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)




def all_categories (request) :

    if request.method =='GET':

        categories = Category.objects.all()
        serializer = CategorySerializer(categories , many =True)
        return JsonResponse(serializer.data, safe = False)

    if request.method == 'POST':
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)