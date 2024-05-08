"""
URL configuration for corporate_assets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from assets.views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    # jwt-authentication
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # Company URLs
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),

    # Device URLs
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-detail'),

    # Employee URLs
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),

    # DeviceAssignment URLs
    path('device-assignments/', DeviceAssignmentListCreateView.as_view(), name='device-assignment-list-create'),
    path('device-assignments/<int:pk>/', DeviceAssignmentRetrieveUpdateDestroyView.as_view(), name='device-assignment-detail'),
    
    #DeviceConditionLogs
    path('device-condition-logs/', DeviceConditionLogListCreateView.as_view(), name='device-condition-log-list-create'),
    path('device-condition-logs/<int:pk>/', DeviceConditionLogRetrieveUpdateDestroyView.as_view(), name='device-condition-log-detail'),

    # for admin
    path("admin/", admin.site.urls),

    # for api authentications
    path('api-auth/', include('rest_framework.urls')),

    # for swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Default URL - Redirect to API schema
    path('', SpectacularAPIView.as_view(), name='default'),


]