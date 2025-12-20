from django.shortcuts import render
from django.views.generic import DetailView, ListView

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
