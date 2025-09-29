from django.db import models


class Status(models.Model):
  BUSSINES = 'B'
  PERSONAL = 'P'
  TAX = 'T'
  status_list = [(BUSSINES, 'Бизнес'), (PERSONAL, 'Личное'), (TAX, 'Налог'),]
  title = models.CharField(max_length=200, choices=status_list)

class Field(models.Model):
  pub_date = models.DateTimeField(auto_now_add=True, editable=True)
  status = models.ForeignKey(
    Status,
    related_name='status',
    on_delete=models.CASCADE,
  )
