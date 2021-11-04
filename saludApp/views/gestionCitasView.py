from django.conf                                    import settings
from django.http                                    import request
from rest_framework                                 import generics, serializers, status
from rest_framework                                 import response
from rest_framework.response                        import Response
from saludApp.models.gestionCitas                   import GestionCitas
from saludApp.serializers.gestionCitasSerializer    import GestionCitasSerializer
from rest_framework.permissions                     import IsAuthenticated
from rest_framework_simplejwt.backends              import TokenBackend

#Clase para ver una cita en especifico
class GestionCitasDetailView(generics.RetrieveAPIView):   
    queryset = GestionCitas.objects.all()
    serializer_class = GestionCitasSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs): 
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)
   
#Clase para ver la lista de citas de un usuario 
class GestionCitasListView(generics.ListAPIView):
    queryset = GestionCitas.objects.all()
    serializer_class = GestionCitasSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self): 
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        queryset = GestionCitas.objects.filter(user_id=self.request.user)
        return queryset

#Clase para Crear cita    
class GestionCitasCreateView(generics.CreateAPIView):
    queryset = GestionCitas.objects.all()
    serializer_class = GestionCitasSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_s401_UNAUTHORIZED)
        serializer=GestionCitasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Cita Guardada con Exito",status=status.HTTP_201_CREATED)

#Clase para actualizar Cita    
class GestionCitasUpdateView(generics.UpdateAPIView):
    queryset = GestionCitas.objects.all()
    serializer_class = GestionCitasSerializer
    permission_classes = (IsAuthenticated,)
    
    def put(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)

#Clase para Eliminar una cita    
class GestionCitasDestroyView(generics.DestroyAPIView):
    queryset = GestionCitas.objects.all()
    serializer_class = GestionCitasSerializer
    permission_classes = (IsAuthenticated,)
    
    def delete(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)