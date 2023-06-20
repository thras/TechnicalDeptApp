from django.urls import path
from .views import SupplierList, SupplierDetail, OrderCreateView,OrderDetailView,OrderListView,OrderUpdateView, MyOrderListView,OrderDetail,OrderList,OrderDeleteView
from .views import SupplierCreateView,SupplierDetailView,SupplierListView,SupplierUpdateView,SupplierDeleteView, CompletedOrderListView, IncompletedOrderListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # API Supplier urls
    path("api/supplier/<int:pk>/", SupplierDetail.as_view(), name="api_supplier_detail"),
    path("api/supplier/", SupplierList.as_view(), name="api_suppliers_list"),

    # API Order urls
    path("api/orders/<int:pk>/", OrderDetail.as_view(), name="api_order_detail"),
    path("api/orders/", OrderList.as_view(), name="api_orders_list"),

    # Front-end Supplier urls
    path('supplier_add/', login_required(SupplierCreateView.as_view()), name='supplier_add'),
    path('supplier_detail/<int:pk>/', login_required(SupplierDetailView.as_view()), name='supplier_detail'),
    path('supplier_list/', login_required(SupplierListView.as_view()), name='supplier_list'),
    path('supplier_edit/<int:pk>/', login_required(SupplierUpdateView.as_view()), name='supplier_edit'),
    path('supplier_delete/<int:pk>/', login_required(SupplierDeleteView.as_view()), name='supplier_delete'),

    # Front-end Order urls
    path('order_add/', login_required(OrderCreateView.as_view()), name='order_add'),
    path('order_detail/<int:pk>/', login_required(OrderDetailView.as_view()), name='order_detail'),
    path('order_list/', login_required(OrderListView.as_view()), name='order_list'),
    path('order_edit/<int:pk>/', login_required(OrderUpdateView.as_view()), name='order_edit'),
    path('my_order_list/', login_required(MyOrderListView.as_view()), name='my_order_list'),
    path('order_delete/<int:pk>/', login_required(OrderDeleteView.as_view()), name='order_delete'),
    path('order_completed/', login_required(CompletedOrderListView.as_view()), name='order_completed'),
    path('order_incompleted/', login_required(IncompletedOrderListView.as_view()), name='order_incompleted'),
    ]