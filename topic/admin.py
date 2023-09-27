from django.contrib import admin
from topic.models import topic


class topicadmin(admin.ModelAdmin):
    list_display = ['topic_name']

admin.site.register(topic,topicadmin)

# # Register your models here.
