from saludApp.models                        import gestionCitas
from saludApp.models.gestionCitas           import GestionCitas
from saludApp.models.user                   import User
from saludApp.serializers.userSerializer    import UserSerializer
from rest_framework                         import serializers
from saludApp.serializers.userSerializer    import UserSerializer

class GestionCitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestionCitas
        fields = ['user','fechaCita', 'horaCita','areaConsulta']
        
    def to_representation(self, obj):     
        gestioncitas = GestionCitas.objects.get(id=obj.id)
        user = User.objects.get(id=gestioncitas.user_id)
        return {
            'user':{
                'id':user.id,
                'name':user.name,
                'email':user.email,               
                'telephone':user.telephone
            },
            'fechaCita':gestioncitas.fechaCita,
            'horaCita':gestioncitas.horaCita,
            'areaConsulta':gestioncitas.areaConsulta,           
        }