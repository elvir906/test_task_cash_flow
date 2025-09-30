from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from .models import Field, Status

def index(request):
    fields = Field.objects.all()
    context = {
        'fields': fields,
        # 'title': title,
        'index': True,
    }
    return render(request, 'index.html', context)

    