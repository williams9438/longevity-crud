from rest_framework import viewsets
from .serializers import UserSerializer
from users.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a specified user. \n
    ***Note:*** \n
    - ***You can use this endpoint to get user using GET Method.*** 

    update:
    Return a update status. \n
    ***Note:*** \n
    - ***You can use this endpoint to update existing user using PUT Method.***
    """
    
    permission_classes = [IsAuthenticated]
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'head', 'post']

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)


class UsersViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a specified user. \n
    ***Note:*** \n
    - ***You can use this endpoint to get user using GET Method.*** 

    update:
    Return a update status. \n
    ***Note:*** \n
    - ***You can use this endpoint to update existing user using PUT Method.***
    """
    
    permission_classes = [IsAuthenticated]
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'head', 'post']