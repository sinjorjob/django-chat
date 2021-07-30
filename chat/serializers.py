from rest_framework import serializers
from accounts.models import CustomUser
from chat.models import Messages


class MessageSerializer(serializers.ModelSerializer):

    sender_name = serializers.SlugRelatedField(many=False, 
                                               slug_field='username', 
                                               queryset=CustomUser.objects.all())
    receiver_name = serializers.SlugRelatedField(many=False, 
                                               slug_field='username', 
                                               queryset=CustomUser.objects.all())

    class Meta:
        model = Messages
        fields = ['sender_name', 'receiver_name', 'description', 'time']

