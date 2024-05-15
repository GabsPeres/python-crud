from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

from rest_framework import status
from rest_framework.response import Response



# List all students
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# List a specific ID    
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
# List API view
class AllStudentsListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Update in request Http    
# Can be partial or not
class StudentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    partial = True

# Delete Student's registration
# Through ID  
class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Student"))



