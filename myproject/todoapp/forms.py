from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    # 設定情報の定義するための内部クラス
    class Meta:
        # 使用するモデルをTodoに定義
        model = Todo
        # 表示するフィールドを定義
        fields = ["title", "memo", "completed"]
        # フィールドのラベルをカスタマイズ
        labels = {
            "title": "タイトル",
            "memo": "メモ",
            "completed": "完了フラグ",
        }
