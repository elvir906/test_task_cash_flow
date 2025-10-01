from django import template
register = template.Library()

@register.simple_tag
def get_verbose_field_name(instance, field_name):
    """
    Возвращает содержимое параметра 'verbose_name' у поля field_name
    таблицы instanse
    """
    return instance._meta.get_field(field_name).verbose_name.title()

# @register.simple_tag
# def get_verbose_field_name_no_meta(instance, field_name):
#     """
#     Возвращает содержимое параметра 'verbose_name' у поля field_name
#     таблицы instanse
#     """
#     return instance._meta.get_field(field_name).verbose_name.title()