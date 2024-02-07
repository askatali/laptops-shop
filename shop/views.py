from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework import generics


from shop.models import Laptop, Image
from shop.serializers import LaptopModelSerializer, CreateLaptopSerializer


class LaptopView(TemplateView):
    template_name = 'laptop.html'
    permission_classes = (AllowAny,)
    serializer_classes = LaptopModelSerializer


    def get_context_data(self, **kwargs):
        # laptops = Laptop.objects.order_by('-price')
        queryset = Laptop.objects.all()
        return {'laptops/<int:id>/': queryset}


class LaptopCreateAPIView(APIView):
    permission_classes = (AllowAny,)
    # queryset = Laptop.objects.all()
    serializer_class = CreateLaptopSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateLaptopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Laptop.objects.create(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)










