from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fastapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 #   url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'books.views.template_two'),
#    url(r'^3/', 'article.views.template_simple_three'),
	url(r'^books/all/$', 'books.views.books'),
	url(r'^authors/all/$', 'books.views.authorsview'),
	url(r'^author/get/(?P<author_id>\d+)/$','books.views.authorview'),
	url(r'^book/get/(?P<book_id>\d+)/$','books.views.bookview'),
	url(r'^style/get/(?P<style_id>\d+)/$','books.views.styleview'),
	url(r'^styles/all/$', 'books.views.stylesview'),
	url(r'^books/addbook/$','books.views.addbook'),
	url(r'^books/add/$','books.views.bookform'),
	url(r'^styles/addstyle/$','books.views.addstyle'),
	url(r'^authors/addauthor/$','books.views.addauthor'),
	url(r'^authors/add/$','books.views.authorform'),
	url(r'^styles/add/$','books.views.styleform'),
	url(r'^styles/delstyle/$','books.views.delstyleform'),
	url(r'^styles/del/$','books.views.delstyle'),
	url(r'^$','books.views.overview'),
#	url(r'^$', 'authors.views.authors'),

)
