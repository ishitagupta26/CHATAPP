from . import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer,UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated







class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            print(f"User {user.username} registered successfully!")
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Retrieve username and password from the validated data
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            # Authenticate the user
            user = authenticate(username=username, password=password)

            if user:
                # Login the user
                login(request, user)

                # Generate tokens
                refresh = RefreshToken.for_user(user)

                # Return the response
                return Response({
                    "status": "success",
                    "data": {
                        "user": UserSerializer(user).data,
                        "access_token": str(refresh.access_token),
                        "refresh_token": str(refresh)
                    }
                }, status=status.HTTP_200_OK)

            # If authentication fails
            return Response({"status": "error", "data": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # If serializer validation fails
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render

# Create your views here.
