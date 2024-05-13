from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'message_id',
            'thread_id',
            'sender_id',
            'user_name',
            'recipient_id',
            'timestamp',
            'text',
            'attachments_json',
            'first_attachment_type',
            'first_attachment_url',
            'status',
            'response_to',
        ]

    message_id = serializers.UUIDField(format='hex')
    thread_id = serializers.UUIDField(format='hex')
    sender_id = serializers.UUIDField(format='hex')
    recipient_id = serializers.UUIDField(format='hex')
    response_to = serializers.UUIDField(format='hex', allow_null=True)