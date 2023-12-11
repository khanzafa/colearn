from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.views.generic import View
from .models import Quiz, Question, Choice, Answer, QuizHistory
from django.contrib import messages
from courses.models import Course
User = get_user_model()

# Create your views here.
class KuisView(View):
    def get(self, request):
        quizzes = Quiz.objects.all()
        jenis = request.GET.get('jenisKuis', None)
        if jenis == 'kuisLatihan':
            quizzes = Quiz.objects.filter(quiz_type='exercise')
        elif jenis == 'kuisUjian':
            quizzes = Quiz.objects.filter(quiz_type='test')        
        
        urutan = request.GET.get('sort', None)
        if urutan == 'newest':
            quizzes = quizzes.order_by('-created_at')
        elif urutan == 'oldest':
            quizzes = quizzes.order_by('created_at')
        
        status = request.GET.get('status', None)
        if status == 'finished':
            quizzes = quizzes.filter(quizhistory__student_id=request.user.id)
        elif status == 'ongoing':
            quizzes = quizzes.exclude(quizhistory__student_id=request.user.id)

        for quiz in quizzes:
            quiz.score = quiz.quizhistory_set.filter(student_id=request.user.id).first().score if quiz.quizhistory_set.filter(student_id=request.user.id).first() else '-'
            quiz.questions_count = quiz.question_set.count()            
        return render(request, 'kuis.html', {'quizzes': quizzes})



class KuisLatihanView(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        quizzes = Quiz.objects.filter(course_id=course_id)
        detail_quiz = []
        for quiz in quizzes:
            questions = Question.objects.filter(quiz_id=quiz.id)
            detail_quiz.append({
                'id': quiz.id,
                'title': quiz.title,
                'description': quiz.description,
                'duration': quiz.duration,
                'questions_count': questions.count(),
                'score': quiz.quizhistory_set.filter(student_id=request.user.id).first().score if quiz.quizhistory_set.filter(student_id=request.user.id).first() else '-'
            })    

        return render(request, 'kuis-latihan.html', {
            'course': course,
            'quizzes': detail_quiz
        })

class KuisDetailView(View):
    def get(self, request, course_id, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        return render(request, 'detail-kuis.html', {'quiz': quiz, 'questions': questions})
    
    def post(self, request, course_id, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        student = request.user
        score = 0

        for question in quiz.question_set.all():
            choice_id = request.POST.get(f'question_{question.id}', None)
            if choice_id:
                choice = get_object_or_404(Choice, id=choice_id)
                Answer.objects.create(quiz=quiz, student=student, question=question, choice=choice)
                if choice.is_correct:
                    score += 1
        
        score = (score / quiz.question_set.count()) * 100
        quiz_history, created = QuizHistory.objects.get_or_create(quiz=quiz, student=student)
        quiz_history.score = score
        quiz_history.save()

        messages.success(request, 'Quiz submitted successfully!')
        return redirect('quizzes:kuis', course_id)


class KuisHasilView(View):
    def get(self, request, quiz_id):
        quiz = Quiz.objects.get(pk=quiz_id)
        questions = Question.objects.filter(quiz_id=quiz.id)
        choices = Choice.objects.filter(question_id=questions[0].id)
        answers = Answer.objects.filter(quiz_id=quiz.id, student_id=request.user.id)
        score = 0
        for answer in answers:
            if answer.choice.is_correct:
                score += 1
        quiz_history = QuizHistory.objects.get(quiz_id=quiz.id, student_id=request.user.id)
        quiz_history.score = score
        quiz_history.save()
        return JsonResponse ({
            'quiz': quiz,
            'questions': questions,
            'choices': choices,
            'answers': answers,
            'score': score
        })
        # return render(request, 'hasil-kuis.html', {
        #     'quiz_history': quiz_history,
        #     'quiz': quiz,
        #     'questions': questions,
        #     'choices': choices,
        #     'answers': answers,
        #     'score': score
        # })