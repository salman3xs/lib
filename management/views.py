from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from management import models
from management.forms import BookForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class BookListView(ListView):
    model = models.Book
    
    def get_queryset(self):
        return models.Book.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class BookDetailView(DetailView):
    model = models.Book

class BookCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'management/book_detail.html'
    form_class = BookForm
    model = models.Book

class BookUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'management/book_detail.html'
    form_class = BookForm
    model = models.Book

class BookDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    success_url = reverse_lazy('book_list')
    model = models.Book
    
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = models.Book
    redirect_field_name = 'management/book_list.html'
    def get_queryset(self):
        return models.Book.objects.filter(published_date__isnull=True)

########################################################################
########################################################################

@login_required
def book_publish_view(request,pk):
    book = get_object_or_404(models.Book,pk=pk)
    book.publish()
    return redirect('book_detail',pk=pk)
