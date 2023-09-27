from django.contrib import admin
from main.models import topic , question


class topicadmin(admin.ModelAdmin):
    list_display = ['topic_name']

class questionadmin(admin.ModelAdmin):
    list_display = ['question_name','question','code','explanation','topic']

admin.site.register(topic,topicadmin)
admin.site.register(question,questionadmin)

# # Register your models here.