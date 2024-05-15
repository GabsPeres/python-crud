from django.urls import path
from .views import StudentListCreateView, StudentDetailView,AllStudentsListView,StudentDeleteView,StudentUpdateView


'''
    /students/ = general access
    /students/id = localize a specific student by ID
    /students/all = return all registration in database
    /students/delete/id = delete a specific registration specifying a ID
    /students/update/id = update a specific registration with Update or Patch (patch is partial)
'''

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='Student-list-create'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='Student-detail'),
    path('students/all/', AllStudentsListView.as_view(), name='all-Students-list'),  
    path('students/delete/<int:pk>', StudentDeleteView.as_view(), name='Student-delete'), 
    path('students/update/<int:pk>', StudentUpdateView.as_view(), name='Student-update'), 
]