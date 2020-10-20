from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # Overriding the create_user method so that the password is stored as a hash
    # instead of plain text in the database:
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user