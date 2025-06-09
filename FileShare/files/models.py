from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class SharedFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def get_share_link(self):
        return f"/view/{self.id}/"
