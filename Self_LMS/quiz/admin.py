from django.contrib import admin
from .models import TFQuestion

@admin.register(TFQuestion)
class TFQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'correct_answer', 'created_at')
    list_filter = ('correct_answer',)
    search_fields = ('text',)


