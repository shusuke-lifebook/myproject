from django.http import HttpResponse
from django.shortcuts import render

from .models import Sample

# Create your views here.


# ===============================================
# サンプルの一覧を表示するビュー
# ===============================================
def sample_list(request):
    # データベースからすべてのSampleを取得
    samples = Sample.objects.all()
    # テンプレートにデータを渡して表示
    return render(request, "appendixapp/list.html", {"samples": samples})


# ===============================================
# 特定サンプルの詳細を表示するビュー
# ===============================================
def sample_detail(request, id):
    # 指定されたidのSampleを取得
    sample = Sample.objects.get(id=id)
    # テンプレートにデータを渡して表示
    return render(request, "appendixapp/detail.html", {"sample": sample})


# ===============================================
# 新しいサンプルを作成するビュー
# ===============================================
def sample_create(request):
    # POSTリクエストの場合
    if request.method == "POST":
        # フォームから送信されたnameの値を取得
        name = request.POST.get("name")
        # 新しいSampleをデータベースに保存
        Sample.objects.create(name=name)
        # 成功したメッセージを画面に表示
        return HttpResponse("作成成功！")

    # GETリクエスト時のフォーム画面を表示
    return render(request, "appendixapp/create.html")
