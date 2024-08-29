from django.urls import path
from .views import UserListView, UserDetailView


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
]


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
]
