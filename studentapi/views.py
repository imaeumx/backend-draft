from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Student
from . serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('student_id')
    serializer_class = StudentSerializer

@api_view(['POST'])
def register_user(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_user(request):
    users = StudentSerializer.objects.all().order_by('student_id')
    serializer = StudentSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)