from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey


class Status(models.Model):
    """Модель для таблицы 'Статус'"""

    value = models.CharField(
        max_length=100,
        blank=False,
        unique=True,
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['value',]

    def __str__(self):
        return self.value


class FlowType(models.Model):
    """Модель для таблицы 'Тип'"""

    value = models.CharField(
        max_length=100,
        blank=False,
        unique=True,
        verbose_name='Тип'
    )

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['value',]
    
    def __str__(self) -> str:
        return self.value


class Category(MPTTModel):
    """Модель для таблицы 'Категория'"""

    value = models.CharField(
        max_length=100,
        blank=False,
        unique=True,
        verbose_name='Категория'
    )

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.PROTECT,
    )

    class MPTTMeta:
        order_insertion_by = ['value']
          

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        # constraints = [
        #   models.UniqueConstraint(
        #     name="unique_category",
        #     # fields=["room", "date"],
        #     include=["full_name"]
        #   )
        # ]

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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        related_name='user_post',
        verbose_name='Пользователь'
    )
    status = models.ForeignKey(
        Status,
        related_name='post_status',
        on_delete=models.CASCADE,
        verbose_name=status_verbose_name_title
    )
    flow_type = models.ForeignKey(
        FlowType,
        related_name='post_flow_type',
        on_delete=models.CASCADE,
        blank=False,
        verbose_name=flow_type_verbose_name_title
    )
    category = models.ForeignKey(
        Category,
        related_name='post_category',
        on_delete=models.CASCADE,
        blank=False,
        verbose_name=category_verbose_name_title
    )
    subcategory = models.ForeignKey(
        Category,
        related_name='post_subcategory',
        on_delete=models.CASCADE,
        blank=False,
        verbose_name=subcategory_verbose_name_title
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False
    )

    class Meta:
        verbose_name = 'Запись о ДДС'
        verbose_name_plural = 'Записи о ДДС'
        ordering = ['pub_date']
      
    def __str__(self) -> str:
        return self.status.value
