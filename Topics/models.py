from __future__ import unicode_literals

from django.db import models


class Topics(models.Model):
    topic_name = models.CharField(max_length=30, default='')
    topic_id = models.IntegerField(null=False, blank=False)
    tutorial_available = models.BooleanField(default=False)
    formulae_available = models.BooleanField(default=False)
    questions_available = models.BooleanField(default=False)
    nbr_of_ques = models.IntegerField(null=False, default=1)
    topic_icon_url = models.CharField(default='/static/Table/img/', max_length=100)
    tutorial_id = models.IntegerField(null=True, primary_key=False, blank=False)
    formulae_id = models.IntegerField(null=True, primary_key=False, blank=False)
    questions_id = models.IntegerField(null=True, primary_key=False, blank=False)


class Numbers(models.Model):
    topic_id = models.ForeignKey(Topics, db_column='topic_id', default=1)
    description = models.CharField(max_length=30)
    num_of_ques = models.IntegerField()
    num_of_points = models.IntegerField()


class ProblemsOnAges(models.Model):
    topic_id = models.ForeignKey(Topics, db_column='topic_id', default=1)
    description = models.CharField(max_length=30)
    num_of_ques = models.IntegerField()
    num_of_points = models.IntegerField()


class Progressions(models.Model):
    topic_id = models.ForeignKey(Topics, db_column='topic_id', default=1)
    description = models.CharField(max_length=30)
    num_of_ques = models.IntegerField()
    num_of_points = models.IntegerField()


class Questions(models.Model):
    topic_id = models.ForeignKey(Topics, db_column='topic_id', default=1)
    description = models.CharField(max_length=150, null=True, default='')


class Formulae(models.Model):
    topic_id = models.ForeignKey(Topics, db_column='topic_id', default=1)
    description = models.CharField(max_length=150, null=True, default='')


class Tutorial(models.Model):
    topic_id = models.ForeignKey(Topics, db_column='topic_id', default=1)
    description = models.CharField(max_length=150, null=True, default='')


