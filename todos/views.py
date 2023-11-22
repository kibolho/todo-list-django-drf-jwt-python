from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object() 
        if todo.owner == request.user:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, *args, **kwargs):
        todo = self.get_object()
        if todo.owner != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = self.get_serializer(todo, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)