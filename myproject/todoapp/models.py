import pandas as pd
from django.db import models
from django_pandas.io import read_frame


# Create your models here.
# Todoモデルを定義
class Todo(models.Model):
    # タイトル：最大30文字の文字列フィールド
    title = models.CharField(max_length=30)

    # メモ：長文テキストフィールド(空でもOK)
    memo = models.TextField(null=True, blank=True)

    # 完了フラグ: 真偽値(Boolean)フィールド(デフォルトは未完了=False)
    completed = models.BooleanField(default=False)

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

    @classmethod
    def get_completion_stats(cls):
        """完了済みおよび未完了のタスク数を集計して返す。"""

        # すべてのタスクを取得
        todos = cls.objects.all()

        # 完了済みタスクの数をカウント
        completed = todos.filter(completed=True).count()

        # 未完了タスクの数をカウント
        not_completed = todos.filter(completed=False).count()

        # 総タスク数
        total = completed + not_completed

        # 完了率を計算
        if total > 0:
            completion_rate = round((completed / total) * 100, 2)
        else:
            completion_rate = 0

        # 統計情報を辞書で返す。
        return {
            "completed": completed,  # 完了済みタスク数
            "not_completed": not_completed,  # 未完了タスク数
            "total": total,  # 総タスク数
            "completion_rate": completion_rate,  # 完了率
        }

    @classmethod
    def get_todos_dataframe(cls):
        """ToDoデータをPandasのDateFromに変換"""

        # すべてのタスクを取得する
        todos = cls.objects.all()

        # DjangoのQuerySetをPandasのDataFrameに変換
        # DataFrameはスプレットのような表形式のデータ構造であり
        # データ分析や可視化を行う際に使用する
        return read_frame(todos)
