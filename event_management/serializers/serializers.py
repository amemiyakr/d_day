from rest_framework import serializers
from event_management.models import Menu


class MenuSerializers(serializers.ModelSerializer):
    sub_menu = serializers.SerializerMethodField()

    def get_sub_menu(self, instance):
        temp_menu_list = Menu.objects.all()
        sub_menu_list = []
        for record in temp_menu_list:
            if record.parent_id == instance.id \
                    and record.id != instance.id:
                sub_menu_dict = {
                    'id': record.id,
                    'title': record.title,
                    'url': record.url,
                    'level': record.level,
                    'order': record.order,
                    'icon': record.icon,
                }
                sub_menu_list.append(sub_menu_dict)
        return sub_menu_list

    class Meta:
        model = Menu
        fields = ('id', 'title', 'url', 'level', 'order', 'sub_menu', 'icon')
