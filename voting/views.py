from django.shortcuts import render
from django.http import JsonResponse
from .models import Candidate , Category, Event , Nominee
from .serializers import CandidateSerializer , CategorySerializer, NomineeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
#@parser_classes([MultiPartParser, FormParser])
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



def all_nominees(request) :

    if request.method == 'GET':

       nominees = Nominee.objects.all()
       serializer = NomineeSerializer ( nominees, many =True, context = {'request': request})
       return JsonResponse(serializer.data, safe = False)
    
    
    if request.method == 'POST':
        serializer = NomineeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status= status.HTTP_201_CREATED)

def all_candidates (request):

    if request.method =='GET':

        Candidates = Candidate.objects.all()
        serializer = CandidateSerializer (Candidates , many =True , context ={'request':request} )
        return JsonResponse (serializer.date , safe = False)

    if request.method == 'POST':
        serializer = CandidateSerializer(data = request.data)
        if serializer.is_valid():
            return Response (serializer.data, status = status.HTTP_201_CREATED)
    

def cast_vote(request, candidate_id):
    # This view assumes you're receiving the candidate's ID for whom the vote is cast.
    candidate = Candidate.objects.get(pk=candidate_id)
    Vote.objects.create(candidate=candidate)
    # Update vote count
    candidate.update_vote_count()
    return HttpResponse("Vote cast successfully!")
