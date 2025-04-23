# core/models.py
from django.db import models
from django.contrib.auth.models import User

class CertificateOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.purpose}"