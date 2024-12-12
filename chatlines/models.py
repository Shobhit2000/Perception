from django.db import models
from django.utils import timezone

# Create your models here.
class Chatlines(models.Model):
    chat_id = models.IntegerField()
    role = models.CharField(max_length=100)
    csv_file_path = models.CharField(max_length=1000)
    chat_text_backend = models.CharField(max_length=10000)
    tokens = models.IntegerField()
    type = models.CharField(max_length=100)
    function_name_called = models.CharField(max_length=1000)
    response_status = models.CharField(max_length=100)
    creation_tms = models.DateTimeField(editable=False)
    last_update_tms = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.creation_tms = timezone.now()
        self.last_update_tms = timezone.now()
        return super(Chatlines, self).save(*args, **kwargs)
    