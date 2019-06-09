from django.urls import path
from .views import ListSongsView

urlpatterns = [
    # path('', views.)
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
