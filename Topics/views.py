from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import Http404
# from django.http import HttpResponse
from serializers import *
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


def home(request):
    return render(request, 'Table/home.html')


class TopicsList(generics.ListCreateAPIView):
    # To Operate on the whole Data in the Table Numbers
    def __init__(self):
        self.queryset = Topics.objects.all()
        self.serializer_class = TopicsSerializer

    def get(self, request, *args, **kwargs):
        numbers = Topics.objects.all()
        serializer = TopicsSerializer(numbers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        numbers = Topics.objects.all()
        serializer = TopicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicsDetail(generics.RetrieveUpdateDestroyAPIView):
    # To operate on single row of a Table Tables
    def __init__(self):
        self.queryset = Topics.objects.all()
        self.serializer_class = TopicsSerializer

    def get_object(self, pk):
        try:
            return Topics.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        number = self.get_object(pk)
        serializer = TopicsSerializer(number)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        number = self.get_object(pk)
        serializer = TopicsSerializer(number, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        number = self.get_object(pk)
        number.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NumberList(generics.ListCreateAPIView):
    # To Operate on the whole Data in the Table Numbers
    def __init__(self):
        self.queryset = Numbers.objects.all()
        self.serializer_class = NumberSerializer

    def get(self, request, format=None):
        numbers = Numbers.objects.all()
        serializer = NumberSerializer(numbers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NumberDetail(generics.RetrieveUpdateDestroyAPIView):
    # To operate on single row of a Table Number
    def __init__(self):
        self.queryset = Numbers.objects.all()
        self.serializer_class = NumberSerializer
        return

    def get(self, request, pk, format=None):
        numbers = Numbers.objects.get(pk=pk)
        serializer = NumberSerializer(numbers)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        numbers = self.get_object(pk)
        serializer = NumberSerializer(numbers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        numbers = self.get_object(pk)
        numbers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProblemsOnAgesList(generics.ListCreateAPIView):
    # To Operate on the whole Data in the Table ProblemsOnAges
    def __init__(self):
        self.queryset = ProblemsOnAges.objects.all()
        self.serializer_class = ProblemsOnAgesSerializer

    def get(self, request, format=None):
        problems_on_ages = ProblemsOnAges.objects.all()
        serializer = ProblemsOnAgesSerializer(problems_on_ages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProblemsOnAgesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProblemsOnAgesDetail(generics.RetrieveUpdateDestroyAPIView):
    # To operate on single row of a Table ProblemsOnAges
    def __init__(self):
        self.queryset = ProblemsOnAges.objects.all()
        self.serializer_class = ProblemsOnAgesSerializer
        return

    def get(self, request, pk, format=None):
        problems_on_ages = ProblemsOnAges.objects.get(pk=pk)
        serializer = NumberSerializer(problems_on_ages)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        problems_on_ages = self.get_object(pk)
        serializer = NumberSerializer(problems_on_ages, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        problems_on_ages = self.get_object(pk)
        problems_on_ages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProgressionsList(generics.ListCreateAPIView):
    # To Operate on the whole Data in the Table Progressions
    def __init__(self):
        self.queryset = Progressions.objects.all()
        self.serializer_class = ProgressionsSerializer

    def get(self, request, format=None):
        progressions = Progressions.objects.all()
        serializer = NumberSerializer(progressions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProgressionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgressionsDetail(generics.RetrieveUpdateDestroyAPIView):
    # To operate on single row of a Table Progressions
    def __init__(self):
        self.queryset = Progressions.objects.all()
        self.serializer_class = ProgressionsSerializer
        return

    def get(self, request, pk, format=None):
        progressions = Progressions.objects.get(pk=pk)
        serializer = ProgressionsSerializer(progressions)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        progressions = self.get_object(pk)
        serializer = ProgressionsSerializer(progressions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        progressions = self.get_object(pk)
        progressions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionsList(generics.ListCreateAPIView):
    # To Operate on the whole Data in the Table Progressions
    def __init__(self):
        self.queryset = Questions.objects.all()
        self.serializer_class = QuestionsSerializer

    def get(self, request, format=None):
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionsDetail(generics.RetrieveUpdateDestroyAPIView):
    # To operate on single row of a Table Questions
    def __init__(self):
        self.queryset = Questions.objects.all()
        self.serializer_class = QuestionsSerializer
        return

    def get(self, request, pk, format=None):
        questions = Questions.objects.get(pk=pk)
        serializer = QuestionsSerializer(questions)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        questions = self.get_object(pk)
        serializer = QuestionsSerializer(questions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        questions = self.get_object(pk)
        questions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TutorialsList(generics.ListCreateAPIView):
    # To Operate on the whole Data in the Table Progressions
    def __init__(self):
        self.queryset = Tutorial.objects.all()
        self.serializer_class = TutorialSerializer

    def get(self, request, format=None):
        tutorials = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorials, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TutorialsDetail(generics.RetrieveUpdateDestroyAPIView):
    # To operate on single row of a Table Questions
    def __init__(self):
        self.queryset = Tutorial.objects.all()
        self.serializer_class = TutorialSerializer
        return

    def get(self, request, pk, format=None):
        tutorials = Tutorial.objects.get(pk=pk)
        serializer = TutorialSerializer(tutorials)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tutorials = self.get_object(pk)
        serializer = TutorialSerializer(tutorials, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tutorials = self.get_object(pk)
        tutorials.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FormulaeList(generics.ListCreateAPIView):
    # To Operate on the whole Data in the Table Progressions
    def __init__(self):
        self.queryset = Formulae.objects.all()
        self.serializer_class = FormulaeSerializer

    def get(self, request, format=None):
        formulae = Formulae.objects.all()
        serializer = FormulaeSerializer(formulae, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FormulaeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormulaeDetail(generics.RetrieveUpdateDestroyAPIView):
    # To operate on single row of a Table Questions
    def __init__(self):
        self.queryset = Formulae.objects.all()
        self.serializer_class = TutorialSerializer
        return

    def get(self, request, pk, format=None):
        formulae = Formulae.objects.get(pk=pk)
        serializer = FormulaeSerializer(formulae)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        formulae = self.get_object(pk)
        serializer = FormulaeSerializer(formulae, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        formulae = self.get_object(pk)
        formulae.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
