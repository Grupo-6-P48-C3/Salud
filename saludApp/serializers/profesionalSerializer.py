from rest_framework import serializers
from saludApp.models.profesional import Profesional
class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ['email', 'name', 'telephone']
    
    def to_representation(self, obj):
        profesional = Profesional.objects.get(id=obj.id)
        return {
            'email':profesional.email,
            'name':profesional.name,
            'telephone':profesional.telephone
        }