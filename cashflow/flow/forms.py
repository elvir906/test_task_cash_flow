from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            # 'pub_date',
            'user',
            'status',
            'type',
            'category',
            'subcategory',
            'amount',
            'comment'
        )
