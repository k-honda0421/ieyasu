from django.db.models import Count,Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, request
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from myapp.models import Post
from myapp.form import PostCreate, UserCreateForm,LoginForm
from django.contrib.auth.models import User

class PostDetailView(DetailView):
    model = Post
    template_name = 'myapp/post_detail.html'
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()
        
# 記事一覧のビュー
class IndexView(ListView):
    model = Post
    # ↓にテーンプレート名が入る
    template_name = 'myapp/index.html'

# 新規登録
class PostInput(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/post_form.html', {'form': PostCreate})

    def post(self, request, *args, **kwargs):
        # formに描いた内容を格納する
        form = PostCreate(request.POST)
        # 保存する前に一旦取り出す
        post = form.save(commit=False)
        # 保存
        post.save()
        # ホームに移動
        return redirect(to='http://127.0.0.1:8000/')

#アカウント作成
class CreateAccount(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('myapp:index')
        return render(request, 'userconf/user_create.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'userconf/user_create.html', {'form': form, })
create_account = CreateAccount.as_view()

#ログイン機能
class AccountLogin(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('myapp:index')
        return render(request, 'userconf/login.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'userconf/login.html', {'form': form, })
account_login = AccountLogin.as_view()
