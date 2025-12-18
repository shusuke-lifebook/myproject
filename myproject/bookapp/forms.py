from django import forms

from .models import Book


# Bookモデルに基づいたフォームを定義
class BookForm(forms.ModelForm):
    # Metaクラスはフォームの設定を定義する内部クラス
    class Meta:
        # フォームに基づくモデルを指定
        model = Book
        # フォームに表示するフィールドを指定
        # ▽▽▽▽ 4.13 ▽▽▽▽
        fields = ["title", "author", "publication_date", "cover_image"]
        # ▽▽▽▽ 4.11 ▽▽▽▽
        labels = {
            "title": "タイトル",
            "author": "著書",
            "publication_date": "出版日",
            "cover_image": "表紙画像",
        }
        # △△△△ 4.13 △△△△
        # △△△△ 4.11 △△△△
        widgets = {"publication_date": forms.DateInput(attrs={"type": "date"})}
