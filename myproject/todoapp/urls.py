from django.urls import path

from . import views

urlpatterns = [
    # 'list'というURLにアクセスすると、views.pyのTodoListViewクラスが呼び出される。
    # name='todo_list'は、このURLパターンに名前を付けている。
    path("list/", views.TodoListView.as_view(), name="todo_list"),
    # '<int:pk>/'というURLにアクセスすると、views.pyのTodoDetailViewクラスが呼び出される
    # '<int:pk>はURLの一部として渡される整数の主キーを意味し、その主キーに基づいて特定のTodoを表示する。
    # name='todo_detail'は、このURLパターンに名前を付けている。
    path("<int:pk>/", views.TodoDetailView.as_view(), name="todo_detail"),
    # 'new'というURLにアクセスすると、views.pyのTodoCreateViewクラスが呼び出される
    # name='todo_new'は、このURLパターンに名前を付けている。
    path("new/", views.TodoCreateView.as_view(), name="todo_create"),
    # '<int:pk>/edit/'というURLにアクセスすると、views.pyのTodoUpdateViewクラスが呼び出される
    # <int:pk>はURLの一部として渡される整数の主キーを意味し、
    # その主キーに基づいて特定のTodoを表示し、編集する。
    path("<int:pk>/edit/", views.TodoUpdateView.as_view(), name="todo_update"),
    # '<int:pk>/delete/'というURLにアクセスすると、views.pyのTodoDeleteViewクラスが呼び出される
    path("<int:pk>/delete/", views.TodoDeleteView.as_view(), name="todo_delete"),
    # 分析ページのURLを追加
    path("analytics/", views.TodoAnalyticsView.as_view(), name="todo_analytics"),
]
