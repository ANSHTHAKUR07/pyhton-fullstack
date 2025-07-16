from rest_framework import serializers
from .models import data

class dataSerializers(serializers.ModelSerializer):
    class Meta :
        model = data
        fields = '__all__'

        