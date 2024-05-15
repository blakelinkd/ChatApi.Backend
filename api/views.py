from datetime import datetime, timezone
import json
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer
from faker import Faker
import json
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message

fake = Faker()

class MessageView(APIView):
    @csrf_exempt
    def get(self, request, format=None):
        messages = Message.objects.all().order_by('-timestamp')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = json.loads(request.body)
        print(data)
        return create_message(request)

@csrf_exempt
def create_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # UUID validation regex pattern
            uuid_pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
        # Validate and convert UUID fields
            thread_id = uuid.UUID(data.get('thread_id')) if data.get('thread_id') and uuid_pattern.match(data.get('thread_id')) else None
            sender_id = uuid.UUID(data.get('sender_id')) if data.get('sender_id') and uuid_pattern.match(data.get('sender_id')) else None
            recipient_id = uuid.UUID(data.get('recipient_id')) if data.get('recipient_id') and uuid_pattern.match(data.get('recipient_id')) else None
            response_to = uuid.UUID(data.get('response_to')) if data.get('response_to') and uuid_pattern.match(data.get('response_to')) else None

            message = Message.objects.create(
                message_id=uuid.uuid4(),
                thread_id=thread_id,
                sender_id=sender_id,
                user_name=data.get('user_name'),
                recipient_id=recipient_id,
                text=data.get('text'),
                attachments_json=data.get('attachments_json', ''),
                first_attachment_type=data.get('first_attachment_type', ''),
                first_attachment_url=data.get('first_attachment_url', ''),
                status=data.get('status'),
                response_to=response_to
            )
            return JsonResponse({'message': 'Message created successfully'}, status=201)
        except (KeyError, ValueError, re.error) as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
