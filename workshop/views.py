from django.urls import reverse, reverse_lazy
from rest_framework import generics
from .models import Repair,Vehicle
from .serializers import RepairSerializer, VehicleSerializer
from accounts.permissions import IsAuthor
from rest_framework.permissions import IsAuthenticated
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

# Repair API's views
class RepairList(generics.ListCreateAPIView):
    """
    Repair list API view, for all the authenticated users
    
    :model:`Repair`.
    """
    permission_classes  = [IsAuthenticated]
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

class RepairDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Repair detail API view, only for the author of the repair
    
    :model:`Repair`.
    """
    permission_classes  = [IsAuthenticated & IsAuthor]
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

# Vehicle API's views
class VehicleList(generics.ListCreateAPIView):
    """
    Vehicle list API view, for all the authenticated users
    
    :model:`Vehicle`.
    """    
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vehicle list API view, for all the authenticated users
    
    :model:`Vehicle`.
    """
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# Repair views
class RepairCreateView(CreateView):
  ''' View to add a new Repair. '''  
  model = Repair
  fields = ("repair_title", "broken_vehicle", "issue", "repairs_made","repair_status" )
  def get_success_url(self):
    return reverse('my_repair_list')
  '''At submit use the current login user as author'''
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
      
class RepairDetailView(DetailView):
  ''' View for the detail of a Repair. '''  
  model = Repair
  fields = '__all__'
  def get_success_url(self):
    return reverse('repair_detail')
  
class RepairListView(ListView):
  ''' View of listing of all the Repairs paginated by 5 per page. '''
  paginate_by = 5
  model = Repair
  ordering = ['-updated_at']
  template_name = "repair_list.html"
  def get_success_url(self):
    return reverse('my_repair_list')

class RepairUpdateView(UpdateView):
  '''
  View for update a Repair.

  Only the author have permission (restriction at html file).
  '''
  model = Repair
  fields = ("repair_title", "broken_vehicle", "issue", "repairs_made", "repair_status")
  template_name = 'workshop/repair_edit.html'
  def get_success_url(self):
    return reverse('my_repair_list')
  '''At submit use the current login user as author'''
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class MyRepairListView(ListView):
  ''' View of listing of all the Repairs of the current user paginated by 5 per page. '''
  paginate_by = 5
  model = Repair
  template_name = "repair_list.html"
  def get_success_url(self):
    return reverse('my_repair_list')
  ''' Filter the Repairs with the author using the login user.'''
  def get_queryset(self):
    return Repair.objects.filter(author=self.request.user).order_by('-updated_at')

class RepairDeleteView(DeleteView):
  ''' 
  View for delete a Repair.
  
  Only the author have permission (restriction at html file). 
  ''' 
  model = Repair
  template_name = "workshop/repair_delete.html"
  success_url = reverse_lazy("my_repair_list")

class CompletedRepairListView(ListView):
  ''' View of listing of all the Repairs that have completed or cancelled paginated by 5 per page. '''
  paginate_by = 5
  model = Repair
  template_name = "repair_list.html"
  ''' Filter the Repairs with their status.'''
  def get_queryset(self):
    return Repair.objects.filter(repair_status__in=['Completed', 'Cancelled']).order_by('-updated_at')

class IncompletedRepairListView(ListView):
  ''' View of listing of all the Repairs that awaiting parts or stand by offer paginated or are incomplete by 5 per page. '''
  paginate_by = 5
  model = Repair
  template_name = "repair_list.html"
  ''' Filter the Repairs with their status.'''
  def get_queryset(self):
    return Repair.objects.filter(repair_status__in=['Waiting parts', 'Stand by', 'Incomplete']).order_by('-updated_at')


#Vehicle views
class VehicleCreateView(CreateView):
  ''' View to add a new Vehicle.'''
  model = Vehicle
  fields = '__all__'
  def get_success_url(self):
    return reverse('vehicle_list')

      
class VehicleDetailView(DetailView):
  ''' View for the detail of a Vehicle.'''
  model = Vehicle
  fields = '__all__'
  def get_success_url(self):
    return reverse('vehicle_list')
  
class VehicleListView(ListView):
  ''' View of listing of all the Vehicle paginated by 5 per page.'''
  paginate_by = 5
  model = Vehicle
  template_name = "vehicle_list.html"

class VehicleUpdateView(UpdateView):
  ''' View for update a Vehicle. '''
  model = Vehicle
  fields = '__all__'
  template_name = 'workshop/vehicle_edit.html'
  def get_success_url(self):
    return reverse('vehicle_list')

class VehicleDeleteView(DeleteView): 
  ''' View for delete a Vehicle.'''
  model = Vehicle
  template_name = "workshop/vehicle_delete.html"
  success_url = reverse_lazy("vehicle_list")

class VehicleHistoryListView(ListView):
  ''' View of listing of all the repairs of the current vehicle paginated by 5 per page. '''
  paginate_by = 5
  ''' Filter the repairs with the selected pk.'''
  def get_queryset(self, **kwargs):
    return Repair.objects.filter(broken_vehicle = self.kwargs['pk'])
  
