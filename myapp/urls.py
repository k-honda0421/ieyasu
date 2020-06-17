# myapp/urls.py

from django.urls import path

from myapp.views import (
    IndexView,
    PostDetailView,
    CategoryListView,
    TagListView,
    TagPostView,
    CategoryPostView
)
app_name = 'myapp'
urlpatterns = [
    # 記事一覧のURL
    path('', IndexView.as_view(), name='index'),
    # 記事のURL
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # カテゴリー一覧のURL
    path('categories/', CategoryListView.as_view(), name='category_list'),
    # タグ一覧のURL
    path('tags/', TagListView.as_view(), name='tag_list'),
    # カテゴリに紐づいた記事の一覧のURL
    path('category/<str:category_slug>/',
        CategoryPostView.as_view(), name='category_post'),
    # タグに紐づいた記事の一覧のURL
    path('tag/<str:tag_slug>/',TagPostView.as_view(),name='tag_post'),
]
