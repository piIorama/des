from django.contrib import admin
from books.models import Author, Book ,Style 
# Register your models here.
admin.site.register(Author)
admin.site.register(Style)

class AuthorsInline(admin.StackedInline):
	model = Author
	extra = 2
class BookAdmin(admin.ModelAdmin):
	fields = ['book_name','book_text','book_style','book_author','book_date']
	list_filter = ['boot_date']
admin.site.register(Book)