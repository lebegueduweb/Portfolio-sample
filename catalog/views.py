
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django. urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from .forms import RenewBookForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    #Book authors
    num_authors = Author.objects.all().count()  # The 'all()' is implied by default.
    #number of visit to this view
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_visits':num_visits
                 },
    )
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model = Book
class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author




class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class UsersGroupListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name ='catalog/bookinstance_list_borrowed_allUsers.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request,pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)
    #Process data only in cas of a 'post request'
    if  request.method == 'POST':
        #Create a form instance and populate it with data from the request also called binding
        form = RenewBookForm(request.POST)
        #checks the validity of the form before processing
        if form.is_valid():
            # process data in form cleaned data
            book_inst.due_back = form.cleaned_data['Renewal-Date']
            book_inst.save()
            #redirect to new url where user sees all borrowed books
            return HttpResponseRedirect(reverse('all-borrowed-and-borrowers'))
        #if this is a GET (or any other method) create a default form
    else:
        Renewal_Date = datetime.date.today() + datetime.timedelta(weeks = 3)
        form = RenewBookForm(initial={'RenewalDate':Renewal_Date})
    return render(request,'catalog/book_renew_librarian.html', {'form':form, 'bookinst':book_inst})

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'05/01/2018',}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    def AddBook(self):
        return self.Book

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'id', 'author', 'year', 'summary', 'isbn', 'genre']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')