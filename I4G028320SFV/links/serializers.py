from .models import Links
from django.contrib.auth.models import Links
from rest_framework import serializers

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"
