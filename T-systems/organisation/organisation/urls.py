"""
in this file we declare all url patterns
through which we have to access data
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import employees.views
import users.views

"""router object creation"""
router = DefaultRouter()

"""register employee viewset with router"""
router.register('employees', employees.views.EmployeeViewSet, basename='employees')
router.register('users', users.views.UserViewSet, basename='users')

"""in this list we have defined all url patterns"""

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='TokenObtainPair'),
    path('verifytoken/', TokenVerifyView.as_view(), name='TokenVerifyView'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='TokenRefreshView'),
    path('auth/', include('rest_framework.urls')),
]





