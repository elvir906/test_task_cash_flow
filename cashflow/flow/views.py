from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from . models import Post
from . utils import page_obj_gen

def index(request):
    posts = Post.objects.all().select_related('status')
    page_obj = page_obj_gen(request, posts)
    title = 'Движение денежных средств'
    context = {
        'page_obj': page_obj,
        'title': title,
        'pub_date_title': Post.pub_date_verbose_name_title,
        'status_title' : Post.status_verbose_name_title,
        'flow_type_title': Post.flow_type_verbose_name_title,
        'category_title': Post.category_verbose_name_title,
        'subcategory_title': Post.subcategory_verbose_name_title,
        # 'index': True,
    }
    return render(request, 'index.html', context)
