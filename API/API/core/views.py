from django.shortcuts import render
from rest_framework import viewsets, permissions, authentication
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()


class IsAuthenticatedOrWriteOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a write-only request.
    """

    def has_permission(self, request, view):
        WRITE_METHODS = ["POST"]

        return (
            request.method in WRITE_METHODS or
            request.user and
            request.user.is_authenticated
        )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticatedOrWriteOnly]

    def check_email(self):
        pass

    def check_sms(self):
        pass


class AddressView(APIView):
    """
    View to check addresses
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        return Response('hello world')