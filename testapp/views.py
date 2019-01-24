from django.shortcuts import render, Http404, HttpResponse
from courseapp.models import CourseModel
from .models import TestModel
from courseapp.models import McqQuestionModel, SubQuestionModel
import random
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from useraccount.decorators import admin_required

from django.utils import timezone

# Create your views here.

@login_required
def test_detail(request, course_name):
    try:
        course_instance = CourseModel.objects.get(name=course_name)
    except CourseModel.DoesNotExist:
        raise Http404("There is no course that matches user's query")
    return render(request, 'testapp/test-details.html',{'course': course_instance})

@login_required
def take_test(request, course_name):
    if request.method == "GET":
        instance, created = TestModel.objects.get_or_create(
            course_id=course_name,
            candidate_id=request.user.email)
        if created:
            instance.save()
        else:
            instance.test_start_time = timezone.now()
            instance.score = 0
            instance.save()
        return render(request, "testapp/test.html", {"course": course_name})

@login_required
def get_questions(request,course_name):
    if request.method == "GET":
        sub_questions_all = list(SubQuestionModel.objects.values('question', 'q_id'))
        mcq_questions_all = list(McqQuestionModel.objects.values(
            'question',
            'q_id',
            'opt_a',
            'opt_b',
            'opt_c',
            'opt_d',
        ))
        all_questions = mcq_questions_all
        all_questions.extend(sub_questions_all)
        questions_random = random.sample(all_questions,30 if len(all_questions)>30 else len(all_questions))

        return JsonResponse(questions_random, safe=False)