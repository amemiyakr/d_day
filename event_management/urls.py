from rest_framework import routers
from django.conf.urls import url
from event_management.views.d_day_list_views import *
from event_management.views.views import MenuView

router = routers.DefaultRouter()
router.register(r"users", UserView)
router.register(r"event-day", EventDayView)

api_route = [
    *router.urls,
    url(r'menu', MenuView.as_view()),
    url(r'get-user-list', GetUserLstView.as_view()),
]
