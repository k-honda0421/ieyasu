# myapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from myapp.views import (
    IndexView,
    PostDetailView,
    PostInput,
    CreateAccount,
    AccountLogin
)
app_name = 'myapp'
urlpatterns = [
    # 記事一覧のURL
    path('', IndexView.as_view(), name='index'),
    # 記事のURL
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # 投稿サイトのURL
    path('post_form/', PostInput.as_view(), name='post_form',),
    # サインインのURL
    path('create_account/', CreateAccount.as_view(), name='signin_form'),
    # ログインURL
    path('login/', AccountLogin.as_view(), name='login_form'),
    # ログアウト
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
