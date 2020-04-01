from rest_framework.views import APIView
from rest_framework.response import Response
from event_management.models import Menu
from event_management.serializers.serializers import MenuSerializers
from django.db.models import F


class MenuView(APIView):

    def get(self, request):
        temp_menu_list = Menu.objects.all().filter(pk=F('parent_id'))
        menu_serializer = MenuSerializers(temp_menu_list, many='true')

        return Response(menu_serializer.data)
