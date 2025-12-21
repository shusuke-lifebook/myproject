from django.shortcuts import render
from django.urls import reverse_lazy  # URL逆引き用のモジュールをインポート
from django.utils.timezone import localtime
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import models


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
# Todo作成用のビュー： 継承元はCreateView
# ========================================================
class TodoCreateView(CreateView):
    # 使用するモデルを指定
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = "todoapp/todo_create.html"
    # フォームで使用するフィールドを指定
    fields = ["title", "memo", "completed"]
    # 登録成功時のリダイレクト先を指定
    success_url = reverse_lazy("todo_list")


# ========================================================
# Todo更新用のビュー： 継承元はUpdateView
# ========================================================
class TodoUpdateView(UpdateView):
    # 使用するモデルを指定
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = "todoapp/todo_update.html"
    # フォームで使用するフィールド
    fields = ["title", "memo", "completed"]
    # 更新成功時のリダイレクト先を指定
    success_url = reverse_lazy("todo_list")

    # フォームのバリデーション(入力チェック)が成功され時に呼ばれるメソッド
    def form_valid(self, form):
        # フォームのデータを保存し、Todoインスタンスを取得
        todo = form.save()
        # ターミナルに更新情報を記録(タイトルと更新時刻)
        print(f"タイトル：'{todo.title}' 更新時間：{localtime(todo.updated)}")
        # 親クラスのform_validを実行し、処理を続行
        return super().form_valid(form)


# ========================================================
# Todo削除用のビュー： 継承元はDeleteView
# ========================================================
class TodoDeleteView(DeleteView):
    # 使用するモデル
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = "todoapp/todo_delete.html"
    # 削除成功時のリダイレクト先を指定
    success_url = reverse_lazy("todo_list")
