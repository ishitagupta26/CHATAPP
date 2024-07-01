from django.urls import path
from .views import message_list, message_detail, user_messages, delete_message

urlpatterns = [
    path('message/', message_list, name='message-list'),
    path('message/<str:receiver>/', message_detail, name='message-detail'),
    path('message/<int:message_id>/delete/', delete_message, name='delete-message'),
    path('user-message/', user_messages, name='user-messages'),
]