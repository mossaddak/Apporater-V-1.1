from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import(
    User
)

#serializer
from .serializer import(
    UserSerializer,
    LoginSerializer
)

#otp verification
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)

# Create your views here.
class SingUp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        'message':"something Went Wrong",
                        'data':serializer.errors
                    },status = status.HTTP_400_BAD_REQUEST
                )
            if serializer.is_valid():
                serializer.save()
                user = User.objects.all().last()
                refresh = RefreshToken.for_user(user)
                return Response(
                    { 
                        'message':"Your account is created.",
                        'data':{
                            'token':{
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                                "is_superuser":user.is_superuser,
                            }

                        }
                    },status = status.HTTP_201_CREATED
                )
        
        except Exception as e:
            print(e)
            return Response(
                    {
                        'message':"something Went Wrong",
                        'message':serializer.errors,
                    },status = status.HTTP_400_BAD_REQUEST
                    
                )
        
class TotalUserView(APIView):
    def get(self, request):
        AllUser = User.objects.all().count()
        return Response(
            {
                'total_user':AllUser,
            },status = status.HTTP_200_OK
            
        )
        

class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        'data':serializer.errors,
                        'message':"something Went Wrong"
                    },status = status.HTTP_400_BAD_REQUEST
                )
            response = serializer.get_jwt_token(serializer.data)
            return Response(response,status = status.HTTP_200_OK)

        except Exception as e:
            return Response(
                    {
                        'error':e,
                        'message':"something Went Wrong"
                    },status = status.HTTP_400_BAD_REQUEST
                )
        

#profile ================================================================>
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        users = User.objects.all()
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def patch(self, request):
        try:
            userid = request.user.id
            user = User.objects.get(pk=userid)
            data = request.data
            serializer = UserSerializer(user, data=data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'user': serializer.data,
                        'message': "Your profile has been updated"
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'user': serializer.errors,
                        'message': "Your profile could not be updated"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        except IntegrityError:
            return Response(
                {
                    'user': None,
                    'message': "A user with that username already exists"
                },
                status=status.HTTP_409_CONFLICT
            )
        
        except Exception as e:
            print(e)
            return Response(
                {
                    'user': None,
                    'message': "An error occurred while updating your profile"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) 
