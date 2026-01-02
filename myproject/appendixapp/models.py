from django.db import models

# Create your models here.


# データベースのテーブルに相当するモデルを定義
class Sample(models.Model):
    # 名前を保持するフィールド
    name = models.CharField(max_length=100)
