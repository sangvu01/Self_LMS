from rest_framework import serializers

from .models import Choice, Chapter, Course, Question, Quiz


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

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
    # course_title = serializers.SerializerMethodField()
    course_title = serializers.CharField(
        source = "course.title",
        read_only = True
    )
    prev_chap_slug = serializers.SerializerMethodField()
    next_chap_slug = serializers.SerializerMethodField()
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
            "course_title",
            "next_chap_slug",
            "prev_chap_slug"
        ]    
    def get_chapters(self, obj):
        ch = obj.course.chapters.all()
        print(type(obj))
        return SideBarChapterSerializer(ch, many = True).data
    def get_course_title(self, obj):
        return obj.course.title
    def get_current_chap(self, obj):
        return obj.slug
    def get_prev_chap_slug(self, obj):
        ch = obj.course.chapters.filter(order__lt=obj.order).order_by("-order").first()
        return ch.slug if ch else None
        # chapters = list(filter(lambda c: c.order < obj.order, obj.course.chapters.all()))
        # return None if (len(chapters) == 0) else chapters[-1].slug
    def get_next_chap_slug(self, obj):
        ch = obj.course.chapters.filter(order__gt=obj.order).order_by("order").first()
        return ch.slug if ch else None
        # return list(filter(lambda x: x.id < obj.id, obj.course.chapters.all()))[-1] if len(list(filter(lambda x: x.id < obj.id, obj.course.chapters.all()))) > 0 else None
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "text", "is_correct"]


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "order", "choices"]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "course", "title", "description", "is_active", "questions"]
