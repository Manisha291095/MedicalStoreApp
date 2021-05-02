from django.db import models

# Create your models here.

class Medicines(models.Model):
    Medicine_code = models.IntegerField()
    Name          = models.CharField(max_length = 40)
    price         = models.FloatField()
    stock         = models.IntegerField()
    medicine_picture = models.FileField()

    class Meta:
        db_table = 'medicines'

    def __str__(self):
        return self.name    
