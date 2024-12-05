from rest_framework import serializers
from .models import Career
from django.core.exceptions import ValidationError

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
        read_only_fields = ['id', 'created_datetime', 'username']  # Explicitly set read-only fields

    def update(self, instance, validated_data):
        # Allowed fields for update
        allowed_fields = ['title', 'content']

        # Compare the fields in the request data (not validated_data) to find invalid fields
        invalid_fields = [field for field in self.initial_data.keys() if field not in allowed_fields]

        # Check for invalid fields and raise validation error
        if invalid_fields:
            raise serializers.ValidationError({
                'invalid_fields': f"These fields cannot be updated: {', '.join(invalid_fields)}"
            })

        # Proceed with the update
        return super().update(instance, validated_data)