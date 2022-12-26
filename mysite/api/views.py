from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from rest_framework import filters


# страница профиля
class DetailUser(APIView):
    # склейка информации о пользователе и заказанных товарах
    def get(self, request, pk):
        user = AdvUser.objects.filter(id=pk).get()
        orders = Order.objects.filter(user=pk).all()
        serializer = UserSerializer(user)
        serializer2 = OrderSerializer(orders, many=True)
        return Response({"user": serializer.data, "orders": serializer2.data})


# регистрация (основная логика в сериалайзере)
class SignUp(generics.CreateAPIView):
    queryset = AdvUser.objects.all()
    serializer_class = UserSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({"message": 'Пользователь создан', "status:": status.HTTP_201_CREATED},
                        status=status.HTTP_201_CREATED, headers=headers)


# все продукты
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter] # поиск
    search_fields = ['name']  # поиск


# один продукт
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


# заказ продукта
class CreateOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        order = Order.objects.create(user=request.user, product=Product.objects.get(pk=pk))
        order.save()
        return Response({"data:": ({"message:": "Продукт заказан"})})
