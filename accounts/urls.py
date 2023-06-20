from django.urls import path
from .views import UserList, UserDetail, register, AccountListView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # API accounts urls
    path("api/user/<int:pk>/", UserDetail.as_view(), name="api_user_detail"),
    path("api/user/", UserList.as_view(), name="api_user_list"),

    # Front-end accounts urls
    path('change_password/', login_required(auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html',success_url = '/')),name='change_password'),
    path('register/', register, name = 'register'),
    path('customuser_list/', login_required(AccountListView.as_view()), name='customuser_list'), 
    ]