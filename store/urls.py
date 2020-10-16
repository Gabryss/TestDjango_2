from django.urls import path

from . import views # import views so we can use them in urls


urlpatterns = [
    path('list/',views.listing, name='list'), # '/store/list' wil call the 'listing' function in 'views.py'
    path('list/<int:album_id>/',views.details), #'/store/list/album_id' will call the 'detail' function in 'views.py'
]