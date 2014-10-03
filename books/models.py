# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink 
from django.core.files.storage import FileSystemStorage
from django.core.validators import RegexValidator
# Create your models here.
#fb = FileSystemStorage(location = '/home/fedor/djangoenv/bin/catalog/books/jpegs')
#fa = FileSystemStorage(location = '/home/fedor/djangoenv/bin/catalog/books/jpegs')

class Author(models.Model):
	class Meta():
		db_table = "author"
	author_name = models.CharField(verbose_name="Имя автора",max_length = 20 )
	author_surname = models.CharField(verbose_name="Фамилия автора",max_length = 20)
	author_text = models.TextField(verbose_name="Описание автора")
	#author_date = models.DateTimeField()
	author_jpg = models.ImageField(upload_to='static/jpegs')

class Style(models.Model):
	class Meta():
		db_table = "style"
	style_name = models.TextField(verbose_name="Название стиля")	
class Book(models.Model):
	class Meta():
		db_table = "book"
	book_name = models.TextField(verbose_name="Название книги", max_length = 20)
	book_text = models.TextField(verbose_name="Аннотация книги")
	#book_date = models.DateTimeField()
	books_jpg = models.ImageField(upload_to='static/jpegs')
	book_author = models.ForeignKey(Author)
	book_style = models.ForeignKey(Style)
	

	