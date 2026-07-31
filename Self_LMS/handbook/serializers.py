from rest_framework import serializers
from .models import Course, Chapter


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"#[""title]

