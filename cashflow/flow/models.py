from django.db import models
from django.utils import formats


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
    verbose_name='Наименование статуса'
  )

  class Meta:
      verbose_name = 'Статус'
      verbose_name_plural = 'Статусы'

  def __str__(self) -> str:
    return self.value


class Field(models.Model):
  pub_date = models.DateField(
    auto_now_add=True,
    editable=True,
    verbose_name='Дата публикации'
  )
  status = models.ForeignKey(
    Status,
    # related_name='statuses',
    on_delete=models.CASCADE,
    null=False,
    editable=True,
    verbose_name='Категория ДДС'
  )

  class Meta:
      verbose_name = 'Запись ДДС'
      verbose_name_plural = 'Записи ДДС'
      ordering = ['pub_date']
  
  # def formatted_datetime(self):
  #   return formats.date_format(self.pub_date, "d.M.Y")

  def __str__(self) -> str:
    return self.status.value
