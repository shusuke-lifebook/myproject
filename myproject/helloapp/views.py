from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# --------------------------------------------------------
# ビュー関数を定義
# "ハロー、Django!"というテキストを含むHTTPレスポンスを返す。
# --------------------------------------------------------
def show_hello(request):
    return HttpResponse("ハロー、Django!")
