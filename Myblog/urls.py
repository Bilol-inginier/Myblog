from django.urls import path
from .views import *

urlpatterns = [
    path('', PostlistView.as_view(), name='index'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail'),
]