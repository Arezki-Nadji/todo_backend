from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user_mangement.serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema

class MeViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
            operation_description='This method return the user object that corresponds to the current user',
            responses={200: UserSerializer,
                       400: 'Bad Request'}
    )
    
    def list(self,request):

        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)
