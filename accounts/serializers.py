from rest_framework import serializers
from .models import UserAccount

class UserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(style={'input_type':'password'}, write_only = True)
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'username', 'password','re_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserAccount(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        re_password = self.validated_data['re_password']
        if password != re_password:
            raise serializers.ValidationError({'password':'Password confirm is Incorrect.'})
        user.set_password(validated_data['password'])
        user.save()
        return user