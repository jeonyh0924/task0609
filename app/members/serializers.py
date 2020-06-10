from django.contrib.auth import get_user_model
from rest_framework import serializers

from members.models import Card
from snippets.models import Snippet

User = get_user_model()


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'user',
            'no'
        ]


class UserSerializer(serializers.ModelSerializer):
    card = CardSerializer(source='card_set', many=True, )

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'password',
                  'created',
                  'card',
                  'email',
                  ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
