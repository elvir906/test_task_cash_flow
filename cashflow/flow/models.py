from django import template
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

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


class FlowType(models.Model):
  class Choice_list(models.TextChoices):
    DEPO = ('Пополнение', 'Пополнение')
    DEBT = ('Списание', 'Списание')

  value = models.CharField(
    choices=Choice_list.choices,
    editable=True,
    max_length=100,
    unique=True,
    null=False,
    verbose_name='Тип'
  )

  class Meta:
    verbose_name = 'Тип'
    verbose_name_plural = 'Типы'

  def __str__(self) -> str:
    return self.value


class Category(MPTTModel):
  class Choice_list(models.TextChoices):
    I = ('Инфраструктура', 'Инфраструктура')
    M = ('Маркетинг', 'Маркетинг')
  
  value = models.CharField(
    choices=Choice_list.choices,
    editable=True,
    max_length=100,
    unique=True,
    null=False,
    verbose_name='Категория'
  )

  parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
  )

  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

  def __str__(self) -> str:
    return self.value


class SubCategory(models.Model):
  class Choice_list(models.TextChoices):
    S1 = ('VPS', 'Proxy')
    S2 = ('Farpost', 'Avito')
  
  value = models.CharField(
    choices=Choice_list.choices,
    editable=True,
    max_length=100,
    unique=True,
    null=False,
    verbose_name='Подкатегория'
  )

  category  = models.ForeignKey(
    'Category',
    related_name="categories",
    on_delete=models.CASCADE
  )

  class Meta:
    verbose_name = 'Подкатегория'
    verbose_name_plural = 'Подкатегории'

  def __str__(self) -> str:
    return self.value


class Post(models.Model):
  pub_date_verbose_name_title = 'Дата создания записи'
  status_verbose_name_title = 'Статус'
  flow_type_verbose_name_title = 'Тип'
  category_verbose_name_title = 'Категория'
  subcategory_verbose_name_title = 'Подкатегория'

  pub_date = models.DateField(
    auto_now_add=True,
    editable=True,
    verbose_name=pub_date_verbose_name_title
  )
  status = models.ForeignKey(
    Status,
    related_name='post_status',
    on_delete=models.CASCADE,
    null=False,
    editable=True,
    verbose_name=status_verbose_name_title
  )
  flow_type = models.ForeignKey(
    FlowType,
    related_name='post_flow_type',
    on_delete=models.CASCADE,
    null=False,
    editable=True,
    verbose_name=flow_type_verbose_name_title
  )
  category = models.ForeignKey(
    Category,
    related_name='post_category',
    on_delete=models.CASCADE,
    null=False,
    editable=True,
    verbose_name=category_verbose_name_title
  )
  subcategory = models.ForeignKey(
    SubCategory,
    related_name='post_subcategory',
    on_delete=models.CASCADE,
    null=False,
    editable=True,
    verbose_name=subcategory_verbose_name_title
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    null=True,
    blank=False
  )

  class Meta:
    verbose_name = 'Запись о ДДС'
    verbose_name_plural = 'Записи о ДДС'
    ordering = ['pub_date']
  
  def __str__(self) -> str:
    return self.status.value
