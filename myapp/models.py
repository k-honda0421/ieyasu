from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    # titleの文字制限を255まで
    title = models.CharField(max_length=255)
    # テキストの入力を受け付ける
    text = models.TextField()
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