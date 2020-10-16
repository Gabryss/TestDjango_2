from django.conf.urls import url

from . import views # import views so we can use them in urls


urlpatterns = [
    url('list/',views.listing), # '/store/list' wil call the 'listing' function in 'views.py'
]