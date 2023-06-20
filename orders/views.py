from django.urls import reverse, reverse_lazy
from rest_framework import generics
from .models import Order,Supplier
from .serializers import OrderSerializer, SupplierSerializer
from accounts.permissions import IsAuthor
from rest_framework.permissions import IsAuthenticated
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

#Order API's views
class OrderList(generics.ListCreateAPIView):
    """
    Order list API view, for all the authenticated users
    
    :model:`Order`.
    """
    permission_classes  = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Order detail API view, only for the author of the order
    
    :model:`Order`.
    """
    permission_classes  = [IsAuthenticated & IsAuthor]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Supplier API's views
class SupplierList(generics.ListCreateAPIView):
    """
    Supplier list API view, for all the authenticated users
    
    :model:`Supplier`.
    """
    permission_classes  = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Supplier list API view, for all the authenticated users
    
    :model:`Supplier`.
    """
    permission_classes  = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


# Order views
class OrderCreateView(CreateView):
  ''' View to add a new Order. '''
  model = Order
  fields = ("order", "order_supplier", "body", "order_status")
  def form_valid(self, form):
    '''At submit use the current login user as author'''
    form.instance.author = self.request.user
    return super().form_valid(form)
  def get_success_url(self):
    return reverse('my_order_list')
      
class OrderDetailView(DetailView):
  ''' View for the detail of an Order. '''
  model = Order
  fields = '__all__'
  def get_success_url(self):
    return reverse('my_order_list')
  
class OrderListView(ListView):
  ''' View of listing of all the Orders paginated by 5 per page. '''
  paginate_by = 5
  model = Order
  ordering = ['-updated_at']
  template_name = "order_list.html"
  def get_success_url(self):
    return reverse('my_order_list')

class OrderUpdateView(UpdateView):
  '''
  View for update an order.

  Only the author have permission (restriction at html file).
  '''
  model = Order
  fields = ("order", "order_supplier", "body", "order_status")
  template_name = 'orders/order_edit.html'
  def get_success_url(self):
    return reverse('my_order_list')
  '''At submit use the current login user as author'''
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)  

class MyOrderListView(ListView):
  ''' View of listing of all the Orders of the current user paginated by 5 per page. '''
  paginate_by = 5
  model = Order
  template_name = "order_list.html"
  def get_success_url(self):
    return reverse('my_order_list')
  ''' Filter the orders with the author using the login user.'''
  def get_queryset(self):
    return Order.objects.filter(author=self.request.user).order_by('-updated_at')

class OrderDeleteView(DeleteView): 
  ''' 
  View for delete an order.
  
  Only the author have permission (restriction at html file). 
  '''
  model = Order
  template_name = "orders/order_delete.html"
  success_url = reverse_lazy("my_order_list")

class CompletedOrderListView(ListView):
  ''' View of listing of all the Orders that have completed or cancelled paginated by 5 per page. '''
  paginate_by = 5
  model = Order
  template_name = "order_list.html"
  ''' Filter the orders with their status.'''
  def get_queryset(self):
    return Order.objects.filter(order_status__in=['Completed', 'Cancelled']).order_by('-updated_at')

class IncompletedOrderListView(ListView):
  ''' View of listing of all the Orders that awaiting delivery or waiting offer paginated or are incomplete by 5 per page. '''
  paginate_by = 5
  model = Order
  template_name = "order_list.html"
  ''' Filter the orders with their status.'''
  def get_queryset(self):
    return Order.objects.filter(order_status__in=['Waiting Offer', 'Awaiting Delivery', 'Incomplete']).order_by('-updated_at')



#Supplier views
class SupplierCreateView(CreateView):
  ''' View to add a new Supplier.'''
  model = Supplier
  fields = '__all__'
  def get_success_url(self):
    return reverse('supplier_list')
      
class SupplierDetailView(DetailView):
  ''' View for the detail of a Supplier. '''
  model = Supplier
  fields = '__all__'
  def get_success_url(self):
    return reverse('supplier_list')
  
class SupplierListView(ListView):
  ''' View of listing of all the Suppliers paginated by 5 per page.'''
  paginate_by = 5
  model = Supplier
  template_name = "supplier_list.html"

class SupplierUpdateView(UpdateView):
  ''' View for update a Supplier.'''
  model = Supplier
  fields = '__all__'
  template_name = 'orders/supplier_edit.html'
  def get_success_url(self):
    return reverse('supplier_list')

class SupplierDeleteView(DeleteView): 
  ''' View for delete a Supplier.'''
  model = Supplier
  template_name = "orders/supplier_delete.html"
  success_url = reverse_lazy("supplier_list")

