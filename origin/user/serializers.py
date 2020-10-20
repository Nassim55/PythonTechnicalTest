# Django imports:
from django.contrib.auth.models import User

# Rest framework imports:
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # Overriding the create_user method so that the password is stored as a hash
    # instead of plain text in the database:
    def create(self, validated_data):
        # Creating the user:
        user = User.objects.create_user(**validated_data)

        # Creating the auth token:
        Token.objects.create(user = user)

        return user