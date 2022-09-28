from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets, status 
from api.serializers import SignupSerializer,ProductSeralizer
from api.models import User,UserProfile, Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter





#It will authenitcate user through email and password
class SignupView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializer




#It will get all product details, can use filter, ordering and searching for product

class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ('id', 'name', 'reviews', 'categories')
    ordering_fields = ('name', 'reviews')
    search_fields = ('name', 'reviews')





