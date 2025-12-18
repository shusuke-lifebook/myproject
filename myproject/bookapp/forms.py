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

        error_messages = {
            "title": {
                "max_length": "「タイトル」は20文字以内で入力してください！",
                "required": "「タイトル」を入力してください！",
            },
            "author": {
                "max_length": "「著者名」は10文字以内で入力してください！",
                "required": "「著者名」を入力してください！",
            },
        }

    # タイトルに対するバリデーション
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "盗作" in title:  # type: ignore
            raise forms.ValidationError("タイトルに'盗作'を含めることはできません。")
        return title

    # フォーム全体を対象にしたバリデーション
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        author = cleaned_data.get("author")

        if title == author:
            raise forms.ValidationError("タイトルと著名者は同じにできません。")
        return cleaned_data
