from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from openpyxl import load_workbook
from .models import Data
from .serializers import DataSerializer, FileUploadSerializer


class UploadFileView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            serializer.process_file(file)
            return Response({"message": "Файл успешно обработан и данные сохранены."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JSONDataView(APIView):
    def get(self, request):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)


class HTMLDataView(APIView):
    def get(self, request):
        data = Data.objects.all()
        return render(request, 'table.html', {'data': data})

