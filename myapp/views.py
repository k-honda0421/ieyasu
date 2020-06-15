from django.db.models import Count,Q
from django.shortcuts import render
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from myapp.models import Post, Category, Tag

class PostDetailView(DetailView):
    model = Post

    # オブジェクトを取得するためのメソッド
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        # 記事が公開されていない、ユーザーの登録もない場合４０４エラー
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


# 記事一覧のビュー
class IndexView(ListView):
    model = Post
    # ↓にテーンプレート名が入る
    template_name = 'myapp/index.html'

# カテゴリー一覧のビュー
class CategoryListView(ListView):
    # 公開されている記事のカテゴリ数ーを取得する
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))

# タグ一覧のビュー
class TagListView(ListView):
    # 公開されている記事のタグ数を取得している
    queryset = Tag.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))    
