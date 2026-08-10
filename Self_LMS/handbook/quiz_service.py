from typing import Dict, List


def calculate_attempt_result(questions, selected_answers: Dict[int, int]):
    review = []
    correct = 0

    for question in questions:
        selected_choice_id = selected_answers.get(question.id)
        selected_choice = None
        correct_choice = None

        for choice in question.choices.all():
            if choice.is_correct:
                correct_choice = choice
            if choice.id == selected_choice_id:
                selected_choice = choice

        is_correct = bool(selected_choice and correct_choice and selected_choice.id == correct_choice.id)
        if is_correct:
            correct += 1

        review.append(
            {
                "question_id": question.id,
                "question_text": question.text,
                "selected_choice_id": selected_choice.id if selected_choice else None,
                "selected_choice_text": selected_choice.text if selected_choice else None,
                "correct_choice_id": correct_choice.id if correct_choice else None,
                "correct_choice_text": correct_choice.text if correct_choice else None,
                "is_correct": is_correct,
            }
        )

    total = len(questions)
    score = round((correct / total) * 100) if total else 0
    return {
        "correct": correct,
        "total": total,
        "score": score,
        "passed": score >= 50,
        "review": review,
    }
