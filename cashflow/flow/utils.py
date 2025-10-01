from django.core.paginator import Paginator


def page_obj_gen(request, posts):
    paginator = Paginator(posts, per_page=20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(number=page_number)
    return page_obj