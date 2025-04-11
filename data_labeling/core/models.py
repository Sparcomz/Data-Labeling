from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('uploader', 'Uploader'),
        ('annotator', 'Annotator'),
        ('reviewer', 'Reviewer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Data(models.Model):
    DATA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('text', 'Text'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('review', 'Review'),
        ('complete', 'Complete'),
    ]
    TASK_TYPE_CHOICES = [
        ('object detection', 'Object Detection'),
        ('text extraction', 'Text Extraction'),
    ]
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_data')
    data_type = models.CharField(max_length=10, choices=DATA_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES)
    task_description = models.TextField()
    text_content = models.TextField(blank=True, null=True)  # For text data
    image_content = models.ImageField(upload_to='images/', blank=True, null=True)  # For image data

class Annotation(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    annotator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='annotations')
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    annotation = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class Review(models.Model):
    DECISION_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    feedback = models.TextField()
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES)

class Stat(models.Model):
    annotator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stats')
    tasks_completed = models.IntegerField(default=0)
    amount_rejected = models.IntegerField(default=0)
    amount_approved = models.IntegerField(default=0)

class AdminAction(models.Model):
    ACTION_TYPE_CHOICES = [
        ('delete data', 'Delete Data'),
        ('override review', 'Override Review'),
        ('manage user', 'Manage User'),
    ]
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_actions')
    target_id = models.IntegerField()
    notes = models.TextField()
    action_type = models.CharField(max_length=20, choices=ACTION_TYPE_CHOICES)