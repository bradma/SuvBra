from rest_framework import serializers
from sb.models import customer

class CustSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer