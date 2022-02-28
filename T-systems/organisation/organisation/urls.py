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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]






"""
magic method
dundor method
re_path(r'^employee/', employees.views.EmployeeList.as_view()),
"""