from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # 「テンプレートの継承」を学習するindex画面を表示するURLパターン
    # 例: /ex05/
    path(
        "",
        TemplateView.as_view(template_name="appendixapp/extends_index.html"),
        name="extends_index",
    ),
    # 「テンプレートの継承」をしたテンプレート！を表示するURLパターン
    # 例: /ex05/one/
    path(
        "one/",
        TemplateView.as_view(template_name="appendixapp/one.html"),
        name="extends_one",
    ),
    # 「テンプレートの継承」をしたテンプレート！を表示するURLパターン
    # 例: /ex05/two/
    path(
        "two/",
        TemplateView.as_view(template_name="appendixapp/two.html"),
        name="extends_two",
    ),
]
