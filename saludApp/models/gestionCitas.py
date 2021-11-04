from django.db  import models
from .user      import User

class GestionCitas(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='gestioncitas', on_delete=models.CASCADE)
    fechaCita = models.DateField()
    horaCita = models.TimeField(['%H:%M'])
    areaConsulta=models.CharField('AreaConsulta',max_length=30)