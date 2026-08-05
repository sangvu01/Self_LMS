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

class SideBarChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ["title", "slug", "order"]

class ChapterDetailSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField()
    current_chap = serializers.SerializerMethodField()
    course_title = serializers.SerializerMethodField()
    class Meta:
        model = Chapter
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "summary",
            "content",
            "course",
            "chapters",
            "current_chap",
            "course_title"
        ]    
    def get_chapters(self, obj):
        ch = obj.course.chapters.all()
        print(type(obj))
        return SideBarChapterSerializer(ch, many = True).data
    def get_course_title(self, obj):
        return obj.course.title
    def get_current_chap(self, obj):
        return obj.slug
