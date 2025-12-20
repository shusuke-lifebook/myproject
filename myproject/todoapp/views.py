from django.shortcuts import render
from django.urls import reverse_lazy  # URL逆引き用のモジュールをインポート
from django.views.generic import CreateView, DetailView, ListView

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
