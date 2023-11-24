from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator


class Chat(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username


class Message(models.Model):
    text = models.CharField(max_length=256, validators=[MinLengthValidator(1)])
    is_reply = models.BooleanField(default=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) < 15:
            return self.text
        return self.text[:11] + ' ...'