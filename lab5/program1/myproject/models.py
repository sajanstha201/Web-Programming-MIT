from django.db import models

class StudentDetail(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of Birth
    address = models.TextField()
    contact_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    
    # Marks for subjects
    physics_marks = models.FloatField()
    english_marks = models.FloatField()
    chemistry_marks = models.FloatField()

    def __str__(self):
        return self.name


