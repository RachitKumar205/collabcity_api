from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from .serializers import PollSerializer
from .models import Idea
from django.contrib.auth.models import User


class PollViewSet(ModelViewSet):
    serializer_class = PollSerializer
    queryset = Idea.objects.all()

    @action(detail=False)
    def get_list(self, request):
        pass

    @action(detail=True)
    def get_Idea(self, request, pk):
        return Idea



