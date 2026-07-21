from types import SimpleNamespace

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import TFQuestion


def quiz_view(request, question_id):
    """Display a single True/False question."""
    question = get_object_or_404(TFQuestion, pk=question_id)
    context = {
        'question': question,
        'question_id': question_id,
    }
    return render(request, 'quiz/question.html', context)


def quiz_preview(request):
    """Render a hardcoded preview of the quiz question UI."""
    preview_question = SimpleNamespace(
        text='The sun rises in the east.',
        correct_answer=True,
    )
    context = {
        'question': preview_question,
        'question_id': 'preview',
        'is_preview': True,
    }
    return render(request, 'quiz/question.html', context)


def quiz_preview_result(request):
    """Render a hardcoded preview of the quiz result UI."""
    preview_question = SimpleNamespace(
        text='The sun rises in the east.',
        correct_answer=True,
    )
    context = {
        'question': preview_question,
        'user_answer': True,
        'is_correct': True,
        'correct_answer': True,
        'is_preview': True,
    }
    return render(request, 'quiz/result.html', context)


def submit_answer(request, question_id):
    """Handle True/False answer submission."""
    if request.method != 'POST':
        return redirect('quiz_view', question_id=question_id)

    question = get_object_or_404(TFQuestion, pk=question_id)

    user_answer_str = request.POST.get('answer')
    if user_answer_str is None:
        return redirect('quiz_view', question_id=question_id)

    try:
        user_answer = user_answer_str.lower() in ('true', '1', 'yes', 'on')
    except Exception:
        user_answer = False

    is_correct = (user_answer == question.correct_answer)

    context = {
        'question': question,
        'user_answer': user_answer,
        'is_correct': is_correct,
        'correct_answer': question.correct_answer,
    }

    return render(request, 'quiz/result.html', context)

def quiz_preview_submit(request):
    return redirect('quiz_preview_result')