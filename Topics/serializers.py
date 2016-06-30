# from django.contrib.auth.models import User

from rest_framework import serializers
from models import *


class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ('id', 'topic_name', 'topic_id', 'tutorial_available', 'formulae_available', 'questions_available',
                  'nbr_of_ques', 'topic_icon_url', 'tutorial_id', 'formulae_id', 'questions_id')


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ('topic_id', 'description', 'num_of_ques', 'num_of_points')


class ProblemsOnAgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemsOnAges
        fields = ('topic_id', 'description', 'num_of_ques', 'num_of_points')


class ProgressionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemsOnAges
        fields = ('topic_id', 'description', 'num_of_ques', 'num_of_points')


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('topic_id', 'description')


class FormulaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulae
        fields = ('topic_id', 'description')


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('topic_id', 'description')
