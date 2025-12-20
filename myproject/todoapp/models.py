from django.db import models


# Create your models here.
# Todoモデルを定義
class Todo(models.Model):
    # タイトル：最大30文字の文字列フィールド
    title = models.CharField(max_length=30)

    # メモ：長文テキストフィールド(空でもOK)
    memo = models.TextField(null=True, blank=True)

    # 完了フラグ: 真偽値(Boolean)フィールド(デフォルトは未完了=False)
    complated = models.BooleanField(default=False)

    # 作成日時: 日時フィールド(自動的に現在時刻が設定される)
    created = models.DateTimeField(auto_now_add=True)

    # 更新日時: 日時フィールド(自動的に現在時刻が設定さえる)
    updated = models.DateTimeField(auto_now=True)

    # オブジェクトの文字列表現を定義(管理画面などでの表示しよう)
    def __str__(self):
        # タイトルを返す
        return self.title

    # モデルのメタ情報を定義
    class Meta:
        # 作成日時の降順でソート(最新が最初)
        ordering = ["-created"]
