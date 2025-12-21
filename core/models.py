from django.db import models
from django.contrib.auth.models import User

# Tools ke liye model
class Tool(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='tools_files/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Admin Profile ke liye model (Ye missing tha isliye error aaya)
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Official Shadow")
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='admin_pics/', null=True, blank=True)

    def __str__(self):
        return self.name