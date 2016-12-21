from django.contrib import admin

from .models import Question, Topic, Answer

# Register models in admin interface
admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(Answer)