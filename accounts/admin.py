from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    '''
    Register the updated/custom form at Django create user page
    '''
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username",
                    "is_staff",
                    "is_technician",
                    "is_orderer", 
                    "is_observer",
                    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("is_technician", "is_orderer", "is_observer",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("is_technician", "is_orderer", "is_observer",)}),)

admin.site.register(CustomUser, CustomUserAdmin)