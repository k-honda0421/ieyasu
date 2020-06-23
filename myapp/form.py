from django import forms
from django.forms import ModelForm

from myapp.models import Post

class PostCreate(forms.ModelForm):
    class Meta:
        # モデルに指定
        model = Post
        # フォームとして表示したいカラム（__all__は全てのカラム）
        fields = ('__all__')

