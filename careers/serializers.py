from rest_framework import serializers
from .models import Career
from django.core.exceptions import ValidationError

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
        read_only_fields = ['id', 'created_datetime']

    def update(self, instance, validated_data):

        allowed_fields = ['title', 'content']


        invalid_fields = [field for field in self.initial_data.keys() if field not in allowed_fields]


        if invalid_fields:
            raise serializers.ValidationError({
                'invalid_fields': f"These fields cannot be updated: {', '.join(invalid_fields)}"
            })


        return super().update(instance, validated_data)