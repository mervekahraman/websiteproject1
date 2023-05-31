from django.shortcuts import render
from .models import Question, Answer


def quiz(request):
    questions = Question.objects.all()
    return render(request, 'answer_questions.html', {'questions': questions})

def submit_quiz(request):
    output = 0
    for question in Question.objects.all():
        selected_answer_id = request.POST.get(f'question_{question.id}')
        selected_answer = Answer.objects.get(pk=selected_answer_id)
        if selected_answer.is_correct:
            output += 1
    return render(request, 'output.html', {'output': output})


