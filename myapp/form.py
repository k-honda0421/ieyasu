from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from myapp.models import Post


class PostCreate(forms.ModelForm):
    class Meta:
        # モデルに指定
        model = Post
        # フォームとして表示したいカラム（__all__は全てのカラム）
        fields = ('__all__')

# ログイン機能作成
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        # htmlの表示を変更する
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        # htmlの表示を変更する
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
