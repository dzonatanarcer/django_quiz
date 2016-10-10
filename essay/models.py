from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from quiz.models import Question


@python_2_unicode_compatible
class Essay_Question(Question):

    answer = models.CharField(
        max_length=100,
        verbose_name=_('correct answer'))

    def check_if_correct(self, guess):
        return self.answer.lower().strip() == guess.lower().strip()

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):
        return str(guess)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Essay style question")
        verbose_name_plural = _("Essay style questions")
