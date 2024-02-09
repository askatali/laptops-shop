from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import TemplateView,ListView
from rest_framework import generics


from shop.models import Laptop, Image
from shop.serializers import LaptopModelSerializer, CreateLaptopSerializer, LaptopDetailSerializer


class LaptopListView(ListView):

    model = Laptop
    template_name = 'laptop.html'
    context_object_name = 'laptops'
    serializer_class = LaptopDetailSerializer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        laptops = Laptop.objects.all()
        serializer = LaptopDetailSerializer(laptops, many=True)
        context['laptops'] = serializer.data
        return context


class LaptopDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = LaptopDetailSerializer
    queryset = Laptop.objects.all()
    lookup_field = 'id'


    # model = Laptop
    # serializer_class = LaptopDetailsSerializer
    # context_object_name = 'laptops'
    # template_name = 'lap_detail.html'
    # queryset = Laptop.objects.all()

    # def get_queryset(self):
    #     laptop = Laptop.objects.get(id=self.kwargs['id'])
    #     serializer = LaptopDetailSerializer(laptop, many=False)
    #     return Response(serializer.data)


class LaptopCreateAPIView(APIView):
    permission_classes = (AllowAny,)
    # queryset = Laptop.objects.all()
    serializer_class = CreateLaptopSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateLaptopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Laptop.objects.create(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LaptopUpdateAPIView(UpdateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = LaptopDetailSerializer
    queryset = Laptop.objects.all()
    lookup_field = 'id'


class LaptopDeleteAPIView(DestroyAPIView):
    perm_classes = (AllowAny,)
    serializer_class = LaptopDetailSerializer
    queryset = Laptop.objects.all()
    lookup_field = 'id'
















