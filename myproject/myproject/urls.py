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
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # 'ex01/'のURLがリクエストされたときに、helloappのURLパターンに委任する
    path("ex01/", include("helloapp.urls")),
    # 'ex02/'のURLがリクエストされたときに、bookappのURLパターンに委任する
    path("ex02/", include("bookapp.urls")),
    # 'ex03/'のURLがリクエストされたときに、todoappのURLパターンに委任する
    path("ex03/", include("todoapp.urls")),
    # menu/というURLにアクセスすると、view.MenuPageViewクラスが呼び出される。
    # name="menu"は、このURLパタンンに名前をつけている
    path("menu/", views.MenuPageView.as_view(), name="menu"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
