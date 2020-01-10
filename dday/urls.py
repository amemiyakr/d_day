from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers
from event_management.views import d_day_list_views
from event_management.urls import api_route as event_management_routes, router

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^api/', include(event_management_routes)),
]

api_route = [
    *router.urls,
    # *human_resources_routes,
    # url(r'auth-user', AuthUserView.as_view()),
    # url(r'searchAddress', SearchAddress.as_view()),
    # url(r'cloud-storages', CloudStorageView.as_view()),
]