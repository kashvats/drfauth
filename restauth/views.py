from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response
from .models import school
from .serializer import school1, register
from rest_framework import generics
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# Create your views here.

class listapi(ListAPIView):
    queryset = school.objects.all()
    serializer_class = school1


class detailapi(RetrieveAPIView):
    queryset = school.objects.all()
    serializer_class = school1


class reg(generics.GenericAPIView):
    serializer_class = register
    queryset = User.objects.all()



    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'msg': 'user created',
                'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializers.errors}, statuc=status.HTTP_400_BAD_REQUEST)


class createapi(CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = school.objects.all()
    serializer_class = school1


class updateapi(UpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = school.objects.all()
    serializer_class = school1


# I use basic authentication here
class deleteapi(DestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = school.objects.all()
    serializer_class = school1
