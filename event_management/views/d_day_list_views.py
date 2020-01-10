from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from event_management.serializers.d_day_list_serializers import *
from event_management.models import *


class UserView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventDayView(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = EventDay.objects.all()
    serializer_class = EventDaySerializer


class GetUserLstView(APIView):

    def get(self, request):
        user_list = User.objects.all()
        serializer = UserSerializer(user_list, many='true')

        return Response(serializer.data)
