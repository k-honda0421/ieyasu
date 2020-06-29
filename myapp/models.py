from django.db import models
from django.utils import timezone



# Create your models here.
# カテゴリモデル
class Category(models.Model):
    name = models.CharField('カテゴリ', max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# タグのモデル
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# 記事のモデル
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    # titleの文字制限を255まで
    title = models.CharField("タイトル", max_length=255)
    # テキストの入力を受け付ける
    text = models.TextField("本文")
    # Postが作られた時間をDBに入れる
    created_at = models.DateField(auto_now_add=True)
    # Post更新される度にその時間を入れる
    updated_at = models.DateField(auto_now=True)

    # -created_atを降順にするクラス
    class Meta:
        ordering = ['-created_at']

    #titleを表示するメソッド
    def __str__(self):
        return self.title


# # タグモデル
# class Tag(models.Model):
#     name = models.CharField("タグ", max_length=20)
#     created = at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name

#     def get_latest_post(self):
#         result = Post.objects.filter(tag=self).order_by('-created_at')[:5]
#         return result
