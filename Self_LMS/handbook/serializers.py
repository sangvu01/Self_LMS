from rest_framework import serializers
from .models import Course, Chapter



class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many = True, read_only = True)
    class Meta:
        model = Course
        fields = "__all__"#[""title]
