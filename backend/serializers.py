from rest_framework import serializers
from backend.models import Phonathon_data

class Phonathon_serializer(serializers.ModelSerializer):
   class Meta:
       model = Phonathon_data
       fields = ('alum_id', 'alum_name', 'phone1', 'phone2', 'phone3', 'duration', 'stud_name', 'ldap')
