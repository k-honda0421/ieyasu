from django.db.models import Count,Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, request
from django.views.generic.detail import DetailView
from django.views import View
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from myapp.models import Post
from myapp.form import PostCreate

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

class PostInput(View):
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


