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
    path("student_list/", views.get_all_students, name="student_list"),
    path("sutdent/<int:id>/", views.get_student_by_id, name="student_detail"),
]
