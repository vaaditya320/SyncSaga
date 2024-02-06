from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default = '')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class StoryBranch(models.Model):
    original_story = models.ForeignKey(Story, on_delete=models.CASCADE)
    branched_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_story.title} - Branch by {self.branched_by.username} at {self.timestamp}"