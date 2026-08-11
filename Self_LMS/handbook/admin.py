from django.contrib import admin

from .models import Choice, Chapter, Course, Question, Quiz, QuizAttempt, QuizAttemptAnswer

admin.site.site_header = "Self LMS Administration"
admin.site.site_title = "Self LMS Admin"
admin.site.index_title = "Quiz and course management"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "level", "duration")
    search_fields = ("title", "slug")


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title", "slug")


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "is_active", "created_at")
    list_filter = ("is_active", "course")
    search_fields = ("title", "description", "course__title")
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz", "order")
    list_filter = ("quiz",)
    search_fields = ("text", "quiz__title")
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("is_correct", "question__quiz")
    search_fields = ("text", "question__text")


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("quiz", "user", "score", "total_questions", "created_at")
    list_filter = ("quiz", "created_at")
    search_fields = ("quiz__title", "user__username")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        recent_attempts = QuizAttempt.objects.select_related("quiz", "user").order_by("-created_at")[:8]
        summary = []
        for attempt in recent_attempts:
            summary.append({
                "quiz": attempt.quiz.title,
                "user": attempt.user.username if attempt.user else "Anonymous",
                "score": attempt.score,
                "created_at": attempt.created_at.strftime("%Y-%m-%d %H:%M"),
            })
        extra_context["quiz_result_dashboard"] = summary
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(QuizAttemptAnswer)
class QuizAttemptAnswerAdmin(admin.ModelAdmin):
    list_display = ("attempt", "question", "selected_choice", "is_correct")
    list_filter = ("is_correct",)
    search_fields = ("question__text", "attempt__quiz__title")
