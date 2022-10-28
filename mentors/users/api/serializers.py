from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )

    password = serializers.CharField(write_only=True, validators=[validate_password])
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 're_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            # email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', )
