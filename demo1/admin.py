from django.contrib import admin
from .models import Book, BookNumber
# Register your models here.
#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['title', 'is_pub']
	list_filter = ['launch_date']
	search_fields = ['title', 'description']
admin.site.register(BookNumber)