from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    url('^accounts/login/$', views.index, name='login'),
    url('^accounts/logout/$', views.AccountsLogout, name='logout'),
    url('^accounts/password_change/$', views.AccountsPasswordChange, name='password_change'),
    url('^accounts/password_change/done/$', views.AccountsPasswordChangeDone, name='password_change_done'),
    url('^accounts/password_reset/$', views.AccountsPasswordReset, name='password_reset'),
    url('^accounts/password_reset/done/$', views.AccountsPasswordResetDone, name='password_reset_done'),
    url('^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.AccountsPasswordResetConfirm, name='password_reset_confirm'),
    url('^accounts/reset/done/$', views.AccountsPasswordResetComplete, name='password_reset_complete'),
]

urlpatterns += [
    url('^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^borrowed/$', views.AllLoanedBooksListView.as_view(), name='all-borrowed'),
]

urlpatterns += [
    url('^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author-create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author-update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author-delete'),
]

urlpatterns += [
    url(r'^book/create/$', views.BookCreate.as_view(), name='book-create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book-update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book-delete'),
]