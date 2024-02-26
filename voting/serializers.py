
from rest_framework import serializers
from .models import Candidate , Category
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name','email']



class CategorySerializer (serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = ['id' , 'event']

