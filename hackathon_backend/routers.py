from api.views import PollViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('idea', PollViewSet, basename="idea")