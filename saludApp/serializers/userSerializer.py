from rest_framework import serializers
from saludApp.models.user import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password', 'name', 'telephone']
        
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'email':user.email,
            'name':user.name,
            'telephone':user.telephone
        }