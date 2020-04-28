from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Book, Comment
from .forms import CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class NewBookListView(ListView):
    queryset = Book.objects.order_by('-id')[:2]
    template_name = 'book/newbooks.html'
    context_object_name = 'books'



class BookListView(ListView):
    model = Book
    template_name = 'book/home.html'

    context_object_name = 'books'


class RandomBookView(ListView):
    queryset = Book.objects.order_by('?')[:4]
    template_name = 'book/random.html'
    context_object_name = 'books'


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'book', 'author', 'image']
    template_name = 'book/create.html'
    success_url = reverse_lazy('home')


class BookUpdate(UpdateView):
    model = Book
    template_name = 'book/update.html'
    fields = ['title', 'book']
    success_url = reverse_lazy('home')
    context_object_name = 'books'


class BookDelete(DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'books'



def book_detail_view(request, pk):
    post = get_object_or_404(Book, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            user_name = request.POST.get('user_name')
            body = request.POST.get('body')
            comment = Comment.objects.create(post=post, user_name=user_name, body=body)
            comment.save()
    else:
        comment_form = CommentForm()

    context = {'posts': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'book/detail.html', context)

