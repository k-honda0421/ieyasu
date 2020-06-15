from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    # インスタンスを作成
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # インスタンス変数を表示させるメソッド
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    # Categoryクラスと紐づけている
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # タグで検索できるようにする
    tag = models.ManyToManyField(Tag, blank=True)
    # titleの文字制限を255まで
    title = models.CharField(max_length=255)
    # テキストの入力を受け付ける
    content = models.TextField()
    # テキストの入力を受け付ける(空白でも可)
    description = models.TextField(blank=True)
    # Postが作られた時間をDBに入れる
    created_at = models.DateField(auto_now_add=True)
    # Post更新される度にその時間を入れる
    updated_at = models.DateField(auto_now=True)
    # Postが掲載された時間をDBに入れる
    published_at = models.DateTimeField(blank=True, null=True)
    # Postを公開しているかをTrue/Falseでステータス表示（公開フラグ）
    is_public = models.BooleanField(default=False)

    # -created_atを降順にするクラス
    class Meta:
        ordering = ['-created_at']

    # saveメソッドを定義
    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args,**kwargs)
    
    #titleを表示するメソッド
    def __str__(self):
        return self.title