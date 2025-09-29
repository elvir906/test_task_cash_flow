from django.db import models


class Status(models.Model):
  val = models.CharField(
    max_length=100,
    blank=False,
    default='Bussiness',
    verbose_name='Статусы',
  )

class Field(models.Model):
  pub_date = models.DateTimeField(auto_now_add=True, editable=True)
  status = models.ForeignKey(
    Status,
    related_name='statuses',
    on_delete=models.CASCADE,
  )
