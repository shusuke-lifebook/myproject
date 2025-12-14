# URLパターンを定義するためのpath関連をインポート
from django.urls import path

# 現在のディレクトリのviewsモジュールをインポート
from . import views

urlpatterns = [
    # 'hello/'のURLがリクエストされたとき
    # viewsでモジュールのshow_hello関数を呼び出す。
    path("hello/", views.show_hello, name="hello")
]
