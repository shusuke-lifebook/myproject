from django import forms

from .models import Book


# Bookモデルに基づいたフォームを定義
class BookForm(forms.ModelForm):
    # Metaクラスはフォームの設定を定義する内部クラス
    class Meta:
        # フォームに基づくモデルを指定
        model = Book
        # フォームに表示するフィールドを指定
        fields = ["title", "author", "publication_date"]
