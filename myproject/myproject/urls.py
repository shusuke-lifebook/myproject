"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # 'exe01/'のURLがリクエストされたときに、helloappのURLパターンに委任する
    path("exe01/", include("helloapp.urls")),
    # 'exe02/'のURLがリクエストされたときに、bookappのURLパターンに委任する
    path("exe02/", include("bookapp.urls")),
    # 'exe03/'のURLがリクエストされたときに、todoappのURLパターンに委任する
    path("exe03/", include("todoapp.urls")),
    # 'exe04/'のURLがリクエストさえたときに、educationappのURLパターンに委任する
    path("exe04/", include("educationapp.urls")),
    # 'exe05/のURLがリクエストさえたときに、appendixappのURLパターンに委任する
    path("exe05/", include("appendixapp.urls")),
    # menu/というURLにアクセスすると、view.MenuPageViewクラスが呼び出される。
    # name="menu"は、このURLパタンンに名前をつけている
    path("menu/", views.MenuPageView.as_view(), name="menu"),
    # ログイン画面のURLパターン
    # ルートURLにアクセスするとLoginViewが呼び出される。
    path("", LoginView.as_view(template_name="login.html"), name="login"),
    # ログアウトのURLパターン
    # 'logout/'というURLにアクセスすると、LogoutViewが呼び出される。
    path("logout/", LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
