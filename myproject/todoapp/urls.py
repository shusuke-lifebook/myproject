from django.urls import path

from . import views

urlpatterns = [
    # 'list'というURLにアクセスすると、views.pyのTodoListViewクラスが呼び出される。
    # name='todo_list'は、このURLパターンに名前を付けている。
    path("list/", views.TodoListView.as_view(), name="todo_list")
]
