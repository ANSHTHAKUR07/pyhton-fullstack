# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Book
# from .serializers import BookSerializers
# from rest_framework.decorators import api_view, authentication_classes,permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from .models import Book
# from .serializers import BookSerializers


# class BookViewset(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers




from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializers

    

@api_view(['GET','POST','PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer =BookSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE','PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "Book not found."}, status =status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializers(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer =BookSerializers(book,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = BookSerializers(book, data=request.data, partial=True)  # <- Note partial=True
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)