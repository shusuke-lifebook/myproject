from django.urls import path

from . import views

# URLパターンのリストを定義
urlpatterns = [
    # 書籍の一覧表示ビューに対応するURLパターン
    # 例： /ex02/
    path("", views.book_list, name="book_list"),
    # 書籍の詳細表示ビューに対応するURLパターン
    # 例: /ex02/1
    path("<int:pk>/", views.book_detail, name="book_detail"),
    # 書籍の新規作成ビューに対応するURLパターン
    # 例: /ex02/new/
    path("new/", views.book_create, name="book_create"),
    # 書籍の更新ビューに対応するURLパターン
    # 例: /ex02/1/edit
    path("<int:pk>/edit/", views.book_update, name="book_update"),
    # 書籍の削除ビューに対応するURLパターン
    # 例; /ex02/1/delete
    path("<int:pk>/delete/", views.book_delete, name="book_delete"),
]
