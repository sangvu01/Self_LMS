from django.db import models

class TFQuestion(models.Model):
    text = models.TextField(help_text="The True/False question text")
    correct_answer = models.BooleanField(
        help_text="True if the correct answer is True, False otherwise"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q{self.id}: {self.text[:50]}..."

    class Meta:
        verbose_name = "True/False Question"
        verbose_name_plural = "True/False Questions"


