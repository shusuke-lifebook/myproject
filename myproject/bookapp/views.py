import os

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book


# Create your views here.
# ==================================================
# 書籍の一覧表示
# ==================================================
def book_list(request):
    # すべての書籍をデータベースから取得
    books = Book.objects.all()
    # 'book_list.html' テンプレートに書籍データを渡して表示
    return render(request, "bookapp/book_list.html", {"book_list": books})


# ==================================================
# 書籍の詳細表示
# ==================================================
def book_detail(request, pk):
    # 指定された主キー(pk)に対応する書籍を取得、存在しない場合は404エラーを返す。
    target = get_object_or_404(Book, pk=pk)
    # 'book_detail.html'テンプレートに書籍データを渡して表示
    return render(request, "bookapp/book_detail.html", {"book": target})


# ==================================================
# 書籍の新規作成
# ==================================================
def book_create(request):
    if request.method == "POST":
        # フォームにPOSTデータをバインド
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # フォームデータが有効であれば
            form.save()
            # 成功メッセージを追加
            messages.success(request, "書籍が正常に登録されました。")
            # 書籍の一覧に画面にリダイレクト
            return redirect("book_list")
    else:
        # Getリクエストの場合は空のフォームを表示
        form = BookForm()
    # "book_form.html"テンプレートにフォームデータを渡して表示
    return render(
        request, "bookapp/book_form.html", {"form": form, "title": "書籍登録"}
    )


# ==================================================
# 書籍の更新
# ==================================================
def book_update(request, pk):
    # 指定された主キー(pk)に対応する書籍を取得、存在しない場合は404エラーを返す。
    target = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # フォームにPOSTデータをバインド
        form = BookForm(request.POST, request.FILES, instance=target)

        if "cover_image-clear" in request.POST:
            # フォームにPOSTデータと既存の書籍データをバインド
            cover_image_delete(target)

        if form.is_valid():
            # フォームデータが有効であれば更新
            form.save()
            # 成功メッセージを追加
            messages.success(request, "書籍が正常に更新されました。")
            # 書籍の一覧画面にリダイレクト
            return redirect("book_list")
    else:
        # Getリクエストの場合は既存の書籍データをフォームに表示
        form = BookForm(instance=target)
    # "book_form.html"テンプレートにフォームデータを渡して表示
    return render(
        request, "bookapp/book_form.html", {"form": form, "title": "書籍編集"}
    )


# ==================================================
# 書籍の削除
# ==================================================
def book_delete(request, pk):
    # 指定された主キー(pk)に対応する書籍を取得、存在しない場合は404エラーを返す。
    target = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # 画像ファイルの削除
        cover_image_delete(target)
        # POSTリクエストの場合、書籍を削除
        target.delete()
        # 成功メッセージを追加
        messages.success(request, "書籍が正常に削除されました。")
        # 書籍の一覧にリダイレクト
        return redirect("book_list")
    # book_confirm_delete.htmlテンプレートに書籍データを渡して表示
    return render(request, "bookapp/book_confirm_delete.html", {"book": target})


# ==================================================
# Message フレームワークのサンプル
# ==================================================
def add_messages(request):
    # 成功メッセージの追加
    messages.success(request, "これは成功メッセージです。")
    # エラーメッセージの追加
    messages.error(request, "これはエラーメッセージです。")
    # 情報メッセージの追加
    messages.info(request, "これは情報メッセージです。")
    # 警告メッセージの追加
    messages.warning(request, "これは警告メッセージです。")
    # デバックメッセージの追加
    messages.debug(request, "これはデバックメッセージです。")
    # メッセージを表示する画面にリダイレクト
    return redirect("display_messages")


# メッセージの表示
def show_dispaly_messages(request):
    return render(request, "bookapp/show_all_messages.html")


# ==================================================
# 画像ファイルの削除
# ==================================================
def cover_image_delete(target):
    # 削除する前に画像ファイルのパスを取得
    if target.cover_image:
        # 画像ファイルのパスを取得
        image_path = os.path.join(settings.MEDIA_ROOT, target.cover_image.path)

        # 画像ファイルが存在する場合は、画像データを削除
        if os.path.exists(image_path):
            os.remove(image_path)
