from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from . models import Post, Status
from . utils import page_obj_gen

def index(request):
    posts = Post.objects.all().select_related('status')
    page_obj = page_obj_gen(request, posts)
    title = 'Движение денежных средств'
    context = {
        'page_obj': page_obj,
        'title': title,
        # 'index': True,
    }
    return render(request, 'index.html', context)

    