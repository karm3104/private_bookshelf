import logging
logger = logging.getLogger(__name__)

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import InquiryForm, BookshelfCreateForm
from .models import Bookshelf
from django.db.models import Q

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy("bookshelf:inquiry")

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class BookshelfListView(LoginRequiredMixin, generic.ListView):
    model = Bookshelf
    template_name = 'book_list.html'
    paginate_by = 3

    # def get_queryset(self):
    #     books = Bookshelf.objects.filter(user=self.request.user).order_by('-updated_at')
    #     return books

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            books = Bookshelf.objects.filter(
                Q(title__icontains=q_word) | 
                Q(auther__icontains=q_word)|
                Q(group__icontains=q_word),user=self.request.user).order_by('-updated_at')
            return books
        else:
            books = Bookshelf.objects.filter(user=self.request.user).order_by('-updated_at')
            return books


class BookshelfDetailView(LoginRequiredMixin, generic.DetailView):
    model = Bookshelf
    template_name = 'book_detail.html'

class BookshelfCreateView(LoginRequiredMixin, generic.CreateView):
    model = Bookshelf
    template_name = 'book_create.html'
    form_class = BookshelfCreateForm
    success_url = reverse_lazy('bookshelf:book_list')

    def form_valid(self, form):
        bookshelf = form.save(commit=False)
        bookshelf.user = self.request.user
        bookshelf.save()
        messages.success(self.request, '本を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "本の作成に失敗しました。")
        return super().form_invalid(form)

class BookshelfUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Bookshelf
    template_name = 'book_update.html'
    form_class = BookshelfCreateForm
    
    def get_success_url(self):
        return reverse_lazy('bookshelf:book_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '本の情報を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "本の情報更新に失敗しました。")
        return super().form_invalid(form)

class BookshelfDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Bookshelf
    template_name = 'book_delete.html'
    success_url = reverse_lazy('bookshelf:book_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "本を削除しました。")
        return super().delete(request, *args, **kwargs)


