from django.db import models
import uuid

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thread_id = models.UUIDField()
    sender_id = models.UUIDField()
    user_name = models.CharField(max_length=255)
    recipient_id = models.UUIDField()
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    attachments_json = models.TextField(null=True, blank=True)
    first_attachment_type = models.CharField(max_length=255, null=True, blank=True)
    first_attachment_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=20)
    response_to = models.UUIDField(null=True, blank=True)