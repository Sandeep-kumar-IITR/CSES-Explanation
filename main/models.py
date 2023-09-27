from django.db import models
from tinymce.models import HTMLField
  
class topic(models.Model):
    topic_name = models.CharField(max_length = 100)
    
  
class question(models.Model):
    question_name = models.CharField(max_length = 100)
    question = models.TextField()
    code = HTMLField()
    explanation = models.TextField()
    topic = models.ForeignKey(topic, on_delete = models.CASCADE)
    
