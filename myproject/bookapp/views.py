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
        form = BookForm(request.POST)
        if form.is_valid():
            # フォームデータが有効であれば
            form.save()
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
        form = BookForm(request.POST, instance=target)
        if form.is_valid():
            # フォームデータが有効であれば更新
            form.save()
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
        # POSTリクエストの場合、書籍を削除
        target.delete()
        # 書籍の一覧にリダイレクト
        return redirect("book_list")
    # book_confirm_delete.htmlテンプレートに書籍データを渡して表示
    return render(request, "bookapp/book_confirm_delete.html", {"book": target})
