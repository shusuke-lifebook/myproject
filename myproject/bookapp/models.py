from django.db import models

# Create your models here.


# Bookモデルの定義
class Book(models.Model):
    # 書籍のタイトル(最大20文字)
    title = models.CharField(verbose_name="タイトル", max_length=20)

    # 著名者(最大10文字)
    author = models.CharField(verbose_name="著者", max_length=10)

    # 出版日
    publication_date = models.DateField(verbose_name="出版日")

    # ▽▽▽▽ 4.12 ▽▽▽▽
    # 画像フィールドを追加
    cover_image = models.ImageField(
        verbose_name="表紙画像", upload_to="book_covers/", blank=True, null=True
    )
    # △△△△ 4.12 △△△△

    # オブジェクトの文字列表現を定義
    def __str__(self):
        # 書籍のタイトルを返す。
        return self.title
