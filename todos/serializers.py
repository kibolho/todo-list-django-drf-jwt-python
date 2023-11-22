from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'is_completed',
            'owner',
        )
        model = Todo