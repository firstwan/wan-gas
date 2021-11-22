from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductList(APIView):
    def get(self, request, format=None):
        customers = Product.objects.all()
        serializer = ProductSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        test_data = request
        test_json = request.data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = ProductSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = ProductSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)