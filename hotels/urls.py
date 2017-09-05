from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/hotels/$',
        views.get_hotel_info,
        name='get_hotel_info'
    ),
    url(
        r'^api/v1/hotels/webhook',
        views.handle_webhook,
        name='handle_webhook'
    ),
    url(
        r'^api/test',
        views.test_api,
        name='test_api'
    ),
]
