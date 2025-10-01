from django import template
from django.db import models

register = template.Library()


class Status(models.Model):
  class Choice_list(models.TextChoices):
    B = ('Бизнес', 'Бизнес')
    P = ('Личное', 'Личное')
    T = ('Налоги', 'Налоги')

  value = models.CharField(
    choices=Choice_list.choices,
    editable=True,
    max_length=100,
    unique=True,
    null=False,
    verbose_name='Статус'
  )

  class Meta:
    verbose_name = 'Статус'
    verbose_name_plural = 'Статусы'

  def __str__(self) -> str:
    return self.value


class Post(models.Model):
  pub_date = models.DateField(
    auto_now_add=True,
    editable=True,
    verbose_name='Дата создания записи'
  )
  status = models.ForeignKey(
    Status,
    related_name='post_status',
    on_delete=models.CASCADE,
    null=False,
    editable=True,
    verbose_name='Статус'
  )

  class Meta:
    verbose_name = 'Запись о ДДС'
    verbose_name_plural = 'Записи о ДДС'
    ordering = ['pub_date']
  
  def __str__(self) -> str:
    print(self.pub_date.)
    return self.status.value
  
