from django.urls import path
from .views import RepairList, RepairDetail, VehicleList, VehicleDetail
from django.contrib.auth.decorators import login_required
from .views import RepairCreateView, RepairDeleteView, RepairDetailView, RepairListView, RepairUpdateView, MyRepairListView, VehicleCreateView, VehicleListView, VehicleDetailView, VehicleUpdateView, VehicleDeleteView, VehicleHistoryListView
from .views import CompletedRepairListView, IncompletedRepairListView

urlpatterns = [
    # API Vehicle urls
    path("api/vehicle/<int:pk>/", VehicleDetail.as_view(), name="api_vehicle_detail"),
    path("api/vehicle/", VehicleList.as_view(), name="api_vehicle_list"),

    # API Repair urls    
    path("api/repair/<int:pk>/", RepairDetail.as_view(), name="api_repair_detail"),
    path("api/repair/", RepairList.as_view(), name="api_repair_list"),

    # Front-end Repair urls
    path('repair_add/', login_required(RepairCreateView.as_view()), name='repair_add'),
    path('repair_list/', login_required(RepairListView.as_view()), name='repair_list'),
    path('my_repair_list/', login_required(MyRepairListView.as_view()), name='my_repair_list'),
    path('repair_detail/<int:pk>/', login_required(RepairDetailView.as_view()), name='repair_detail'),
    path('repair_edit/<int:pk>/', login_required(RepairUpdateView.as_view()), name='repair_edit'),
    path('repair_delete/<int:pk>/', login_required(RepairDeleteView.as_view()), name='repair_delete'),
    path('repair_completed/', login_required(CompletedRepairListView.as_view()), name='repair_completed'),
    path('repair_incompleted/', login_required(IncompletedRepairListView.as_view()), name='repair_incompleted'),

    # Front-end Vehicle urls
    path('vehicle_add/', login_required(VehicleCreateView.as_view()), name='vehicle_add'),
    path('vehicle_list/', login_required(VehicleListView.as_view()), name='vehicle_list'),
    path('vehicle_detail/<int:pk>/', login_required(VehicleDetailView.as_view()), name='vehicle_detail'),
    path('vehicle_edit/<int:pk>/', login_required(VehicleUpdateView.as_view()), name='vehicle_edit'),
    path('vehicle_delete/<int:pk>/', login_required(VehicleDeleteView.as_view()), name='vehicle_delete'),
    path('vehicle_history/<int:pk>/', login_required(VehicleHistoryListView.as_view()), name='vehicle_history'),
    ]