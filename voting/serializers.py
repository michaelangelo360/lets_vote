
from rest_framework import serializers
from .models import Candidate , Category , Nominee , Event
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'



class CategorySerializer (serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = ['id' ,'name', 'event']



class NomineeSerializer(serializers.ModelSerializer):
     class Meta:

        model = Nominee
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


    