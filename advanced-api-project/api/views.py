from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Book
from django.urls import reverse_lazy
from .forms import BookForm 

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html' 

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html' 

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html' 
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html' 
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')