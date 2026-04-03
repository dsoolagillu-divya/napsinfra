from django.db import models

# Create your models here.
class JobApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    about = models.TextField()

    def __str__(self):
        return self.full_name
