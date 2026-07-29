from django.db import models

# Create your models here.

# django rest framework
class Course(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    duration = models.CharField(max_length=20)
    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES
    )

    def __str__(self):
        return f"{self.title}"
    def debug_str(self):
        return f"=======================\n\nSlug: {self.slug} \nTitle: {self.title}\n\n======================="

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="chapters")
    order = models.PositiveIntegerField(db_index=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(blank=True, default="")
    summary = models.TextField(blank=True, default="")
    content = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["course", "slug"],
                name="unique_chapter_slug_per_course",
            ),
            models.UniqueConstraint(
                fields=["course", "order"],
                name="unique_chapter_order_per_course",
            )
        ]

    def debug_str(self):
        return f"=======================\n\nChapter: {self.order} \nSlug: {self.course.slug} \nTitle: {self.title}\n\n======================="
    def __str__(self):
        # return f"\nChapter: {self.order} \nSlug: {self.course.slug} \nTitle: {self.title}\n"
        return f"{self.order}.(Course : {self.course})_____ {self.title}"
