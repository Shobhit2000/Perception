from django.db import models
from django.utils import timezone
from user.models import User

# Create your models here.
class Chats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    chat_title = models.CharField(max_length=10000)
    cost = models.FloatField()
    creation_tms = models.DateTimeField(editable=False)
    last_update_tms = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.creation_tms = timezone.now()
        self.last_update_tms = timezone.now()
        return super(Chats, self).save(*args, **kwargs)
    