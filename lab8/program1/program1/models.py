from django.db import models
class DIR(models.Model):
    url=models.CharField()
    num_visited=models.IntegerField()
    num_like=models.IntegerField()
    