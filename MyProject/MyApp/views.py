from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic import DetailView


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'





class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
