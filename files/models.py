from django.db import models
from django.utils import timezone
from datetime import datetime
from user.models import User

class Files(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.FileField()
    creation_tms = models.DateTimeField(editable=False, default=datetime.now())
    last_update_tms = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.creation_tms = timezone.now()
        self.last_update_tms = timezone.now()
        return super(Files, self).save(*args, **kwargs)