from django.contrib import admin
from .models import Author, Book
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    #faqat id da link bor
    list_display = ("id", "first_name", "last_name", "birth_date", "created_at")

    #barchasida link bor
    #list_display_links = ("id", "first_name", "last_name", "birth_date", "created_at")

    #dynamic izlaydi
    search_fields = ("id", "first_name", "last_name")

    #birinchi familiya bo'yicha keyin ism bo'yicha tartiblaydi
    #ordering = ("last_name", "first_name")

    #id bo'yicha tartiblaydi
    ordering = ("id",)
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "slug", "description", "author", "price", "count", "created_at")
    list_display_links = ("id", "title", "slug", "description", "author", "price", "count", "created_at")

