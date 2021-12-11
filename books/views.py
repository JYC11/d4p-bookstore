from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book
from django.db.models import Q

#the mixin should be put on the left so that whether the user is
#logged in is checked first before showing the list view
class BookListView(LoginRequiredMixin,ListView): 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

#same as above but with permissions
class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q') #getting the query parameter
        return Book.objects.filter(
            Q(title__icontains=query)|Q(author__icontains=query)
        )