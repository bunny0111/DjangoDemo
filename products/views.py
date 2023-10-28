from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.views import APIView

# Create your views here.
class ProductAPI(APIView):
    def get(self, request):
        # objs = Product.objects.filter(color__isnull = False)
        data = request.data
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors) 
       
    

    def put(self, request):
        data = request.data
        product_id = data.get('id')

        if product_id is not None:
            try:
                obj = Product.objects.get(productid=product_id)  # Use 'productid' to query
                serializer = ProductSerializer(obj, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=400)
            except Product.DoesNotExist:
                return Response({'message': 'Product not found'}, status=404)
        else:
            return Response({'message': 'Invalid data, "id" is required'}, status=400)


    def patch(self, request):
        data = request.data
        product_id = data.get('id')

        if product_id is not None:
            try:
                obj = Product.objects.get(productid=product_id)  # Use 'productid' to query
                serializer = ProductSerializer(obj, data=data, partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=400)
            except Product.DoesNotExist:
                return Response({'message': 'Product not found'}, status=404)
        else:
            return Response({'message': 'Invalid data, "id" is required'}, status=400)
    
    # def delete(self, request):
    #     data = request.data
    #     obj = Product.objects.get(id=data['id'])
    #     obj.delete()
    #     return Response({'message' : 'Product deleted.'})


    def delete(self, request):
        data = request.data
        product_id = data.get('id')  # Use 'id' to refer to the primary key

        if product_id is not None:
            try:
                obj = Product.objects.get(productid=product_id)  # Use 'productid' to query
                obj.delete()
                return Response({'message': 'Product deleted.'})
            except Product.DoesNotExist:
                return Response({'message': 'Product not found'}, status=404)
        else:
            return Response({'message': 'Invalid data, "id" is required'}, status=400)