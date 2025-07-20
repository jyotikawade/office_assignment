"""all import statement"""
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from .employee_operations import CreateEmployee, DisplayEmployee, UpdateEmployee, DeleteEmployee
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        parameter_dict = request.query_params
        if 'ename' in parameter_dict.keys():
            filtering_data = parameter_dict['ename']
            all_employee_obj = Employee.objects.filter(ename=filtering_data)
            serializer = EmployeeSerializer(all_employee_obj, many=True)
            return Response(serializer.data)
        elif 'eaddr' in parameter_dict.keys():
            filtering_data = parameter_dict['eaddr']
            all_employee_obj = Employee.objects.filter(eaddr=filtering_data)
            serializer = EmployeeSerializer(all_employee_obj, many=True)
            return Response(serializer.data)
        else:
            all_employee_obj = Employee.objects.all()
            serializer = EmployeeSerializer(all_employee_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        id = pk
        ret_value = DisplayEmployee(id)
        if ret_value == status.HTTP_404_NOT_FOUND:
            return Response({'msg': 'not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(ret_value, status=status.HTTP_200_OK)

    def create(self, request):
        ret_value = CreateEmployee(request)
        if ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        ret_value = UpdateEmployee(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        elif ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
        return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        id = pk
        ret_value = UpdateEmployee(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        elif ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
        return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        id = pk
        ret_value = DeleteEmployee(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id in url or in body'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'data deleted'}, status=status.HTTP_200_OK)

# ------------------------------------------------------------------------------------------------------------
