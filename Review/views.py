from itertools import product
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from .serializer import ReviewSerializer
from .models import Review
from rest_framework import status
from django.shortcuts import get_object_or_404
from Review import serializer
from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import mixins
# from rest_framework import generics

@api_view(['GET','POST'])
def ReviewList(request):

    if request.method == 'GET':
        review = Review.objects.filter(Review = product)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])       
def ReviewDetail(request,fk):
    review = get_object_or_404(Review, product_id=fk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class ReviewList(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


# class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer  