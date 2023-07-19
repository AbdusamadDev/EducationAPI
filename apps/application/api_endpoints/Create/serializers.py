from rest_framework import serializers

from apps.application.models import Application



class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        exclude = ("user",)
