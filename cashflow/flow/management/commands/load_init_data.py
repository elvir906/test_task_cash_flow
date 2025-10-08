import json
import os
import sys

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404


from flow.models import Category, Status, FlowType, Subcategory

DATA_ROOT = os.path.join(settings.BASE_DIR, 'flow/data')


class Command(BaseCommand):
    """
    Парсер и загрузчик начальных данных для загрузки названий
    категорий, статусов и типов
    """

    models = ['Category', 'Status', 'FlowType']

    def add_arguments(self, parser):
        print('При наличии нужных файлов, будут загружены начальные данные в'
              f'соответствующие таблицы из {DATA_ROOT} из следующих файлов:')
        for model in self.models:
            filename =  model + '.json'
            parser.add_argument(
                model,
                default = filename,
                nargs = '?',
                type = str
            )
            print(filename)

    def handle(self, *args, **options):
        try:
            for model in self.models:
                with open(
                    os.path.join(DATA_ROOT, options[model]),
                    'r', encoding='utf-8'
                ) as f:
                    data = json.load(f)
                    modelname = getattr(sys.modules[__name__], model)
                    for item in data:
                        print(item)
                        try:
                            if model == 'Category':
                                if item["parent"] == "":
                                    modelname.objects.create(
                                        value=item["name"]
                                    )
                                elif item["parent"] != "":
                                    Subcategory.objects.create(
                                        value=item["name"],
                                        category = get_object_or_404(Category, value=item["parent"])
                                    )
                            else:
                                modelname.objects.create(value=item["name"])
                        except IntegrityError:
                            print(f'Название {item["name"]} уже есть в базе')
        except FileNotFoundError:
            raise CommandError(f'Файл отсутствует в директории {DATA_ROOT}')
