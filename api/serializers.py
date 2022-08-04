from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        read_only_fields  = ('email',)
        fields = (
            'id', 'last_login', 'first_name', 'last_name', 'username', 'gender', 
            'mobile_phone', 'email', 'image', "terms_and_condition", "business_name", "about",
        )