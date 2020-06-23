# myapp/urls.py
from . import views
from django.urls import path

from myapp.views import (
    IndexView,
    PostDetailView,
    PostInput,
)
app_name = 'myapp'
urlpatterns = [
    # 記事一覧のURL
    path('', IndexView.as_view(), name='index'),
    # 記事のURL
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # 投稿サイトのURL
    path('post_form/', PostInput.as_view(), name='post_form',),
]
