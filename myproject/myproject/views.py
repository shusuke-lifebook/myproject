from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# =======================================================
# メニュー画面用のビュー：継承元はTemplateView + LoginRequiredMixin
# =======================================================
class MenuPageView(LoginRequiredMixin, TemplateView):
    # 使用するテンプレートファイルを指定
    template_name = "menu.html"
