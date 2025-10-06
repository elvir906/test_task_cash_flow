import json
import os
import sys

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404


from flow.models import Category, Status, FlowType

DATA_ROOT = os.path.join(settings.BASE_DIR, 'flow/data')


class Command(BaseCommand):
    """
    Парсер и загрузчик начальных данных для загрузки названий
    категории, статусов и типов
    """
    help = 'Загрузка начальных данных'
    models = ['Category', 'Status', 'FlowType']

    def add_arguments(self, parser):
        print(f'Будут загружены начальные данные из {DATA_ROOT} в следующие таблицы:')
        for model in self.models:
            parser.add_argument(model, default=model+'.json', nargs='?', type=str)
            print(model+'.json')

    def handle(self, *args, **options):
        try:
            for model in self.models:
                with open(os.path.join(DATA_ROOT, options[model]), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data:
                        print(item)
                        try:
                            title = getattr(sys.modules[__name__], model)
                            if model == 'Category':
                                if item["level"] == 1:
                                    title.objects.create(value=item["name"], level=item["level"])
                                elif item["level"] == 2:
                                    title.objects.create(value=item["name"], level=item["level"], parent=get_object_or_404(Category, value=item["parent"]))
                            else:
                                title.objects.create(value=item["name"])
                        except IntegrityError:
                            print(f'Название {item["name"]} уже есть в базе')
        except FileNotFoundError:
            raise CommandError('Файл отсутствует в директории data')
