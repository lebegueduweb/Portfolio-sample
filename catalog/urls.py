from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
path('catalog', views.index, name='index'),
path('books/', views.BookListView.as_view(), name='books'),
path('authors/', views.AuthorListView.as_view(), name='authors'),
path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
path('book/>', views.AuthorDetailView.as_view(), name='Details'),
path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
path('accounts/', include('django.contrib.auth.urls')),
path(r'borrowed/', views.UsersGroupListView.as_view(), name='all-borrowed-and-borrowers'),
path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
path('book/create/', views.BookCreate.as_view(), name='book_create'),
path('book/<int:pk>/update/', views.BookCreate.as_view(), name='book_create'),
path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)