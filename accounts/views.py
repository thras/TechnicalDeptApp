from django.shortcuts import redirect, render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSuper
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

#CustomUser API's views
class UserList(generics.ListAPIView):
    """
    CustomUser list API view
    
    Note: only list (create/update/delete are disabled)

    View ONLY for admins(superusers).
    
    :model:`CustomUser`.
    """
    permission_classes  = [IsSuper]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.ListAPIView):
    """
    CustomUser detail API view

    Note: only list (create/update/delete are disabled)
    
    View ONLY for admins(superusers)
    
    :model:`CustomUser`.
    """
    permission_classes  = [IsAuthenticated & IsSuper]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class AccountListView(ListView):
    """
    CustomUser list view
  
    :template:`customuser_list.html`

    :model:`CustomUser`.
    """
    paginate_by = 5
    model = CustomUser
    template_name = "customuser_list.html"



@login_required
def register(request):
    '''
    View to create a new user, use the custom form NewUserForm.

    :model:`CustomUser`.
    '''
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customuser_list')
    else:
        form = NewUserForm()
        return render(request, 'register.html',{'form': form})
