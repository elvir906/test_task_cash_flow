from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from . models import Post, Status, Type, Category, Subcategory
from . forms import PostForm
from . utils import page_obj_gen

def index(request):
    posts = Post.objects.all()
    page_obj = page_obj_gen(request, posts)
    title = 'Движение денежных средств'
    context = {
        'page_obj': page_obj,
        'title': title,
        'pub_date_field_title': Post.pub_date_verbose_name_title,
        'user_field_title': Post.user_verbose_name_title,
        'status_field_title' : Post.status_verbose_name_title,
        'type_field_title': Post.flow_type_verbose_name_title,
        'category_field_title': Post.category_verbose_name_title,
        'subcategory_field_title': Post.subcategory_verbose_name_title,
        'amount_field_title': Post.amount_verbose_name_title,
        'comment_field_title': Post.comment_verbose_name_title
        # 'index': True,
    }
    return render(request, 'index.html', context)

@login_required
def post_create(request):
    form = PostForm (
        request.POST or None
    )
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('cashflow:index')
    title = 'Новая запись'
    context = {
        'form': form,
        'is_edit': False,
        'title': title
    }
    return render(request, 'post_create.html')
