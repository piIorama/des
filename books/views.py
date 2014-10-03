from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context	
from django.shortcuts import render_to_response , redirect
from books.models import Author, Book , Style
from django.core.exceptions import ObjectDoesNotExist
from forms import BookForm , AuthorForm , StyleForm , DelStyleForm
from django.core.context_processors import csrf
from django.contrib import auth
# Create your views here.
def basic_one(request):
	view = "basic_one"
	html = "<html><body>This is %s view</body></html>"% view
	return HttpResponse(html)
def authorsview(request, author_id=1 ,author_name =1):
	return render_to_response('authors.html',{'books':Book.objects.all(),'authors':Author.objects.all(),'styles':Style.objects.all()})
def authorview(request, author_id=1 ,author_name =1):
	args ={}
	args['authors']=Author.objects.filter(id=author_id)
	args['books']=Book.objects.all()
	args['styles']=Style.objects.all() 
	return render_to_response('author.html', args)	
def template_two(request,book_id=1):
	view = "template_two"
	t = get_template ('myview.html')
	html = t.render(Context({'name': Book.objects.get(id=book_id)}))
	return HttpResponse(html)
def books(request,id=1):
	#book_form = BookForm
	args ={}
	args.update(csrf(request))
	args['books']=Book.objects.all()
	args['authors']=Author.objects.all()
	args['styles']=Style.objects.all()
	args['username']=auth.get_user(request).username
	#args['form']=book_form
	return render_to_response('books.html',args)	
def bookview(request, book_id=1):
	return render_to_response('book.html',{'book':Book.objects.filter(id=book_id),'authors':Author.objects.all(),'styles':Style.objects.all()})
def styleview(request, style_id=1):
	return render_to_response('style.html',{'book':Book.objects.all(),'authors':Author.objects.all(),'styles':Style.objects.filter(id=style_id)})
def overview(request):
	return render_to_response('overview.html',{'username': auth.get_user(request).username,'books':Book.objects.all(),'authors':Author.objects.all(),'styles':Style.objects.all()})
def stylesview(request, style_id=1):
	return render_to_response('styles.html',{'book':Book.objects.all(),'authors':Author.objects.all(),'styles':Style.objects.all()})
def addbook(request,id=1):
	if request.POST:
		form = BookForm(request.POST)
		if form.is_valid():
			book=form.save(commit=False)
			form.save()
	return redirect('/books/all',)
def addauthor(request,id=1):
	if request.POST:
		form = AuthorForm(request.POST)
		if form.is_valid():
			author=form.save(commit=False)
			form.save()
	return redirect('/authors/all',)	
def bookform(request,id=1):
	book_form = BookForm
	args ={}
	args.update(csrf(request))
	args['books']=Book.objects.all()
	args['authors']=Author.objects.all()
	args['styles']=Style.objects.all()
	args['form']=book_form
	return render_to_response('addbook.html',args)	
def addstyle(request,id=1):
	if request.POST:
		form = StyleForm(request.POST)
		if form.is_valid():
			style=form.save(commit=False)
			form.save()
	return redirect('/styles/all',)
def delstyle(request,style_id=1):
	if request.POST:
		form = DelStyleForm(request.POST)
		Style.objects.get('id=style_id').delete
		if form.is_valid():
			if style_id==form.cleaned_data.get('style_name',None):
				form.save()
				
	return redirect('/styles/all',)	
def delstyleform(request,style_id=1):
	style_form = StyleForm
	args ={}
	args.update(csrf(request))
	args['books']=Book.objects.all()
	args['authors']=Author.objects.all()
	args['styles']=Style.objects.filter(id=style_id)
	args['form']=style_form
	return render_to_response('delstyle.html',args)	
def styleform(request,id=1):
	style_form = StyleForm
	args ={}
	args.update(csrf(request))
	args['books']=Book.objects.all()
	args['authors']=Author.objects.all()
	args['styles']=Style.objects.all()
	args['form']=style_form
	return render_to_response('addstyle.html',args)

def authorform(request,id=1):
	author_form = AuthorForm
	args ={}
	args.update(csrf(request))
	args['books']=Book.objects.all()
	args['authors']=Author.objects.all()
	args['styles']=Style.objects.all()
	args['form']=author_form
	return render_to_response('addauthor.html',args)	


	