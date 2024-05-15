from django.db import models

# Create your models here.

'''
    This part is defined to receive the data and to storage:
    name = Student's name
    registration = Number of identify the Strundent in system
    birthDate = date field, the number is necessary YYYY-MM-DD
    email = eletronic communication
    phone = don't necessary de code of country, just the complete number and code of city
    entryDate = equal birthDate, unique difference is, the date of entry of course
    course = name of the respective course 
'''

class Student(models.Model):
    name = models.CharField(max_length=50)
    registration = models.PositiveIntegerField()
    birthDate = models.DateField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    entryDate = models.DateField()
    course = models.CharField(max_length=20)

    # This is defined to how is presented in HTML test (that's for internal test)
    def __str__(self):
        return self.registration + " " + self.name + " " + self.course + " " + self.entryDate
