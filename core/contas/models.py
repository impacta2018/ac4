from django.db import models

# Create your models here.
class Curso (models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=140)

    def _str_(self):
        return self.email