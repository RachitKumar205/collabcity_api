from .models import Idea
from rest_framework import serializers
from django.contrib.auth.models import User

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = '__all__'

        def create(self, data):
            return Idea.objects.create(data)

        def update(self, instance, data):
            instance.name = data.get('name', instance.name)
            instance.likes = data.get('likes', instance.likes)
            instance.dislikes = data.get('dislikes', instance.dislikes)
            instance.save()
            return instance

