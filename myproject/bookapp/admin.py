from django.contrib import admin

from .models import Book


# Bookモデルの管理画面をカスタマイズするクラス
class BookAdmin(admin.ModelAdmin):
    # 表示するフィールド
    list_display = ("title", "author", "publication_date")

    # 検索フィールドを指定
    search_fields = ("title", "author")

    # フィルタリングするフィールドを指定
    list_filter = ("publication_date",)


# Register your models here.
admin.site.register(Book, BookAdmin)
