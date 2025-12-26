import base64
import io

import matplotlib
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy  # URL逆引き用のモジュールをインポート
from django.utils.timezone import localtime
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import models
from .forms import TodoForm

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Create your views here.
# ========================================================
# Todo一覧表示用のビュー： 継承元はListView
# ========================================================
class TodoListView(ListView):
    # 使用するモデルを指定(Todoモデル)
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = "todoapp/todo_list.html"
    # テンプレートで使用するオブジェクトリストの名前を指定
    context_object_name = "todos"


# ========================================================
# Todo詳細表示用のビュー： 継承元はDetailView
# ========================================================
class TodoDetailView(DetailView):
    # 使用するモデルを指定(Todoモデル)
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = "todoapp/todo_detail.html"
    # テンプレートで使用するオブジェクトの名前を指定
    context_object_name = "todo"


# ========================================================
# Todo作成用のビュー： 継承元はCreateView + SuccessMessageMixin
# ========================================================
class TodoCreateView(SuccessMessageMixin, CreateView):
    # 使用するモデルを指定
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = "todoapp/todo_create.html"
    # フォームで使用するフィールドを指定
    # fields = ["title", "memo", "completed"]
    # TodoFormクラスを使用する
    form_class = TodoForm
    # 登録成功時のリダイレクト先を指定
    success_url = reverse_lazy("todo_list")
    # 成功メッセージを設定
    success_message = "ToDoが「登録」されました。"


# ========================================================
# Todo更新用のビュー： 継承元はUpdateView + SuccessMessageMixin
# ========================================================
class TodoUpdateView(SuccessMessageMixin, UpdateView):
    # 使用するモデルを指定
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = "todoapp/todo_update.html"
    # フォームで使用するフィールド
    # fields = ["title", "memo", "completed"]
    # TodoFormクラスを使用する
    form_class = TodoForm
    # 更新成功時のリダイレクト先を指定
    success_url = reverse_lazy("todo_list")
    # 成功メッセージを設定
    success_message = "ToDoが「更新」されました。"

    # フォームのバリデーション(入力チェック)が成功され時に呼ばれるメソッド
    def form_valid(self, form):
        # フォームのデータを保存し、Todoインスタンスを取得
        todo = form.save()  # type: ignore
        # ターミナルに更新情報を記録(タイトルと更新時刻)
        print(f"タイトル：'{todo.title}' 更新時間：{localtime(todo.updated)}")
        # 親クラスのform_validを実行し、処理を続行
        return super().form_valid(form)


# ========================================================
# Todo削除用のビュー： 継承元はDeleteView + SuccessMessageMixin
# ========================================================
class TodoDeleteView(SuccessMessageMixin, DeleteView):
    # 使用するモデル
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = "todoapp/todo_delete.html"
    # 削除成功時のリダイレクト先を指定
    success_url = reverse_lazy("todo_list")
    # 成功メッセージを設定
    success_message = "ToDoが「削除」されました。"


# ========================================================
# タスク分析用のビュークラス
# View: Djangoの基本的なビュークラス
# ========================================================
class TodoAnalyticsView(View):
    # 使用するテンプレート
    template_name = "todoapp/todo_analytics.html"

    # GETリクエスト(ページの表示)が来たときに実行されるメソッド
    def get(self, request, *args, **kwargs):
        # -------- ① データ取得 --------
        # Todoモデルから完了、未完了の統計データを取得
        stats = models.Todo.get_completion_stats()
        # -------- ② グラフの作成 --------
        # グラフの枠組みだけ作成
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        # -------- 左側の円グラフの作成 --------
        # グラフのラベル設定
        labels = ["Complated", "Incomplete"]
        # グラフの値
        sizes = [stats["completed"], stats["not_completed"]]
        # グラフの色設定
        colors = ["#66FF99", "#FF3399"]
        # 円グラフを描画
        ax1.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
        # 円グラフを真円に保つ設定
        ax1.axis("equal")
        # グラフのタイトルを設定
        ax1.set_title("Task Completion Rate")

        # -------- 右側の棒グラフの作成 --------
        # TodoモデルからデータをDataForm形式で取得
        df = models.Todo.get_todos_dataframe()
        # データが存在する場合のみグラフを作成
        if not df.empty:
            # 作成日の日付部分だけを取り出して新しい列を作成
            # df['created']にはDateTime型のデータが入っているので
            # .dt.dateで日付部分を取り出す
            df["created_date"] = df["created"].dt.date  # type: ignore
            # 作成日ごとにタスク数をカウント
            # groupby('created_date'): 作成日でグループ化
            # size(): 各グループのタスク数をカウント
            daily_counts = df.groupby("created_date").size()

            # 最新の7件のみを取得
            recent_counts = daily_counts.tail(7)

            # Y軸の最大値を5に設定
            ax2.set_ylim(0, 5)

            # 棒グラフを描画
            recent_counts.plot(kind="bar", ax=ax2, color="#4e73df")

            # x軸のラベルを回転させて重なりを防ぐ
            plt.xticks(rotation=20)

            # タイトルと軸ラベルを英語で設定
            ax2.set_title("Recent Task Creation")
            ax2.set_ylabel("Number of Tasks")
            ax2.set_xlabel("Creation Date")

            # ------ ③ グラフをイメージデータに変換 ------
            # メモリ上に一時的なバッファを作成
            buffer = io.BytesIO()
            # グラフのレイアウトを調整(グラフ同士が重ならないように)
            plt.tight_layout()
            # グラフをPNG形式で一時バッファに保存
            plt.savefig(buffer, format="png")
            # バッファの読み取り位置を先頭に戻す
            buffer.seek(0)
            # バッファからイメージデータを取得
            image_png = buffer.getvalue()
            # バッファを閉じる
            buffer.close()

            # イメージデータをBase64形式(テキスト形式)に変換
            # これによりHTMLに直接埋め込めるようになる
            graph = base64.b64encode(image_png).decode("utf-8")

            # ------ ④ テンプレートにデータを渡す ------
            context = {
                "stats": stats,
                "graph": graph,
            }

            return render(request, self.template_name, context)
