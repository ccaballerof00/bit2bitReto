from django.shortcuts import render
from .models import Question, Answer
from django.forms.models import model_to_dict
from django.utils import timezone
import json
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    return render(request, 'index.html')

def search_results(request):
    keyword = request.POST.get('keyword')

    matches = list(Question.objects.filter(Title__contains=keyword).order_by("-CreationDate"))

    lista = []
    for match in matches:
        lista.append(model_to_dict(match))
    context = {"questions": json.dumps(lista,  cls=DjangoJSONEncoder)}
    return render(request, 'search_results.html', context)

def open_create_question_form(request):
    return render(request, 'create_question.html')

def create_question(request):
    author = request.POST.get('author')
    title = request.POST.get('title')
    description = request.POST.get('description')

    question = Question(
        Author = author,
        Title = title,
        Description = description,
        CreationDate = timezone.now(),
        Answers = []
    )
    question.save()
    context = model_to_dict(question)

    return render(request, 'read_question.html', context)

def read_question(request, id):
    question = Question.objects.get(pk=id)
    context = model_to_dict(question)
    answersids = question.Answers
    answers = []
    if answersids != None:
        for aid in answersids: 
            answers.append(model_to_dict(Answer.objects.get(pk=aid)))
        context["AnswerObjects"] = json.dumps(answers, cls=DjangoJSONEncoder)
    return render(request, 'read_question.html', context)

def submit_answer(request):
    questionid = request.POST.get('Question_Id')
    author = request.POST.get('Author')
    description = request.POST.get('Description')
    answer = Answer(
        Author = author,
        Description = description,
        CreationDate = timezone.now()
    )
    answer.save()
    question = Question.objects.get(pk=questionid)
    question.Answers.append(answer.Answer_Id)
    question.save()
    return read_question(request, questionid)