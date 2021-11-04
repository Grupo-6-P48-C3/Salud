from django.db import models
from .user import User
from .profesional import Profesional

class AutorizacionFormulas(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='autorizacionformulas', on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, related_name='profesional', on_delete=models.CASCADE)
    fechaFormula = models.DateField()
    formula = models.CharField('Formula',max_length=30)
    cantidad = models.IntegerField('Cantidad',null=False)
