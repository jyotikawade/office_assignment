"""all import statement"""
from rest_framework.response import Response
from rest_framework import status
from .user_operations import DisplayUser, CreateUser, UpdateUser, DeleteUser
from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        all_User_obj = Users.objects.all()
        serializer = UserSerializer(all_User_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        id = pk
        ret_value = DisplayUser(id)
        if ret_value == status.HTTP_404_NOT_FOUND:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(ret_value, status=status.HTTP_200_OK)

    def create(self, request):
        ret_value = CreateUser(request)
        if ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'User record created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        ret_value = UpdateUser(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id in url or in body'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        elif ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
        return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        id = pk
        ret_value = UpdateUser(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id in url or in body'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        elif ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
        return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        id = pk
        ret_value = DeleteUser(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id in url or in body'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'data deleted'}, status=status.HTTP_200_OK)
