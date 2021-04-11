from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quizzes(models.Model):
    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True

class Question(Updated):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Indermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choices')),
    )

    quiz = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of Question"))
    title =  models.CharField(max_length=255, verbose_name=_("Quiz Title"))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_('Difficulty'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))
   
   
    def __str__(self):
        return self.title
   
   
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']


class Answer(Updated):
    question = models.ForeignKey(Question, default=1, on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Quiz Title"))
    is_right = models.BooleanField(default=False)
       
    def __str__(self):
        return self.answer_text
   
   
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']