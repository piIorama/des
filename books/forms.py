from django.forms import ModelForm
from models import Book,Author,Style
class BookForm(ModelForm):
	class Meta:
		model =  Book;
		fields = ['book_name','book_text','book_style','book_author']
class AuthorForm(ModelForm):
	class Meta:
		model =  Author;
		fields = ['author_name','author_text','author_surname',]
class StyleForm(ModelForm):
	class Meta:
		model =  Style;
class DelStyleForm(ModelForm):
	class Meta:
		model =  Style;
		