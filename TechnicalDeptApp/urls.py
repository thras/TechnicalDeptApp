"""
URL configuration for TechnicalDeptApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),

    # Project apps urls
    path("", include("accounts.urls")),
    path("", include("orders.urls")),
    path("", include("workshop.urls")),

    # Authentication and login/logout pages
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

    # Home page
    re_path(r'^$', views.index, name='index'),

    # Docstrings urls
    path("api/schema/",  login_required(SpectacularAPIView.as_view()), name="schema"),
    path("api/schema/redoc/",  login_required(SpectacularRedocView.as_view(url_name="schema")), name="redoc",),
    path("api/schema/swagger/",  login_required(SpectacularSwaggerView.as_view(url_name="schema")), name="swagger"),

]

