from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # ORMを学習するindex画面を表示するURLパターン
    path(
        "",
        TemplateView.as_view(template_name="educationapp/orm_index.html"),
        name="orm_index",
    ),
    # 生徒一覧表示するビューに対応するURLパターン
    path("students/", views.get_all_students, name="student_list"),
]
