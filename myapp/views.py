from django.db.models import Count,Q
from django.shortcuts import render, get_object_or_404
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

# カテゴリに紐づいた記事の一覧のビュー
class CategoryPostView(ListView):
    model = Post
    template_name = 'myapp/category_post.html'

    # カテゴリに紐づいた記事を取得するメソッド
    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    # 上記メソッドで取得したデータをテンプレートへ渡すメソッド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

# タグに紐づいた記事の一覧のビュー
class TagPostView(ListView):
    model = Post
    template_name = 'myapp/tag_post.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tag=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
