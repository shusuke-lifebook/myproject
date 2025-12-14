from django.db import models

# Create your models here.


# Bookモデルの定義
class Book(models.Model):
    # 書籍のタイトル(最大20文字)
    title = models.CharField(max_length=20)

    # 著名者(最大10文字)
    author = models.CharField(max_length=10)

    # 出版日
    publication_date = models.DateField()

    # オブジェクトの文字列表現を定義
    def __str__(self):
        # 書籍のタイトルを返す。
        return self.title
