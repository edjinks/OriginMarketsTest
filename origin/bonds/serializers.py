from rest_framework import serializers
from .models import Bond

class BondSerializer(serializers.Serializer):
    isin = serializers.CharField(max_length=12)
    size = serializers.IntegerField()
    currency = serializers.CharField(max_length=3, default='GBP')
    maturity = serializers.DateField()
    lei = serializers.CharField(max_length=20)
    legal_name = serializers.CharField(required=False) #not required for POST will be automatically found from LEI
   
    def create(self, validated_data):
        return Bond.objects.create(**validated_data)
