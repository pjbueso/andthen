from django.db import models

# Create your models here.
class historia(models.model):
    tag = models.CharField(max_length=128, default = "untitled")
    timeStamp  = models.DateTimeField(auto_now_add=True)

class fragmento(models.model):
    content = models.TextField()
    Fecha = models.DateTimeField(auto_now_add=True)
