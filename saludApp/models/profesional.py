from django.db import models

class Profesional(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField('Email', max_length = 100, unique=True)
    name = models.CharField('Name', max_length = 60)
    telephone = models.BigIntegerField('Telephone',null=True)