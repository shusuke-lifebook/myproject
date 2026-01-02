from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # 「テンプレートの継承」を学習するindex画面を表示するURLパターン
    # 例: /exe05/
    path(
        "",
        TemplateView.as_view(template_name="appendixapp/extends_index.html"),
        name="extends_index",
    ),
    # 「テンプレートの継承」をしたテンプレート！を表示するURLパターン
    # 例: /exe05/one/
    path(
        "one/",
        TemplateView.as_view(template_name="appendixapp/one.html"),
        name="extends_one",
    ),
    # 「テンプレートの継承」をしたテンプレート！を表示するURLパターン
    # 例: /exe05/two/
    path(
        "two/",
        TemplateView.as_view(template_name="appendixapp/two.html"),
        name="extends_two",
    ),
    # サンプルのリストを表示するURLパターン
    # /exe05/samples/
    path("samples/", views.sample_list, name="sample_list"),
    # 特定のサンプルの詳細を表示するURLパターン
    # /exe05/samples/1/ (1はサンプルのID)
    path("samples/<int:id>/", views.sample_detail, name="sample_detail"),
    # 新しいサンプルを作成するURLパターン
    # /exe05/samples/create/
    path("samples/create/", views.sample_create, name="sample_create"),
]
