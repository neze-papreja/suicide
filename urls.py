from django.urls import path, reverse_lazy
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.MessageListView.as_view(), name='all_messages')
]
