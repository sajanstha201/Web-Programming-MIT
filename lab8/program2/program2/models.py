from django.db import models
class workModel(models.Model):
    person_name=models.CharField()
    companry_name=models.CharField()
    salary=models.IntegerField()
class livesModel(models.Model):
    person_name=models.ForeignKey(workModel,on_delete=models.CASCADE)
    street=models.CharField()
    city=models.CharField()