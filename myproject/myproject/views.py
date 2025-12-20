from django.views.generic import TemplateView


# =======================================================
# メニュー画面用のビュー：継承元はTemplateView
# =======================================================
class MenuPageView(TemplateView):
    # 使用するテンプレートファイルを指定
    template_name = "menu.html"
