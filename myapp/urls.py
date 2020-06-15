# myapp/urls.py

from django.urls import path

from myapp.views import IndexView, PostDetailView, CategoryListView, TagListView

app_name = 'myapp'
urlpatterns = [
    # 記事一覧のURL
    path('', IndexView.as_view(), name='index'),
    # 記事のURL
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # カテゴリー一覧のURL
    path('categories/', CategoryListView.as_view(), name='category_list'),
    # タグ一覧のビュー
    path('tags/', TagListView.as_view(), name='tag_list'),
]