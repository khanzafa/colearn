from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Quiz, Question, Choice, Answer, QuizHistory
User = get_user_model()

# Create your views here.
def kuis(request):
    quizzes = Quiz.objects.all()
    return render(request, 'kuis.html', {
        'quizzes': quizzes
    })

def detailKuis(request):
    # quiz_id = request.GET.get('quiz_id')
    quiz_id = 1
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz.id)
    choices = Choice.objects.filter(question_id=questions[0].id)
    return render(request, 'detail-kuis.html', {
        'quiz': quiz,
        'questions': questions,
        'choices': choices
    })

def kuisLatihan(request):
    quizzes = Quiz.objects.all()
    return render(request, 'kuis.html', {
        'quizzes': quizzes
    })

def detailKuisLatihan(request):
    # quiz_id = request.GET.get('quiz_id')
    quiz_id = 1
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz.id)
    choices = Choice.objects.filter(question_id=questions[0].id)
    return render(request, 'detail-kuis.html', {
        'quiz': quiz,
        'questions': questions,
        'choices': choices
    })

def hasilKuisLatihan(request):
    # quiz_id = request.GET.get('quiz_id')
    quiz_id = 1
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz.id)
    choices = Choice.objects.filter(question_id=questions[0].id)
    answers = Answer.objects.filter(quiz_id=quiz.id, student_id=request.user.id)
    score = 0
    for answer in answers:
        if answer.choice.is_correct:
            score += 1
    # quiz_history = QuizHistory.objects.get(quiz_id=quiz.id, student_id=request.user.id)
    # quiz_history.score = score
    # quiz_history.save()
    quiz_history = QuizHistory.objects.all()
    return render(request, 'hasil-kuis.html', {
        'quiz_history': quiz_history
    })
    # return render(request, 'hasil-kuis.html', {
    #     'quiz': quiz,
    #     'questions': questions,
    #     'choices': choices,
    #     'answers': answers,
    #     'score': score
    # })