from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Forum, Comment


class ForumListView(ListView):
    model = Forum
    template_name = 'forum/forum.html'  # <app>/<mnodel>_<viewtype>.html
    context_object_name = 'forum_posts'
    ordering = ['-created_at']
    paginate_by = 4


class ForumDetailView(DetailView):
    model = Forum
    comments = Comment.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('-created_at')
        return context


class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ForumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Forum
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        forum = self.get_object()
        if self.request.user == forum.user:
            return True
        return False


class ForumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Forum
    success_url = '/'

    def test_func(self):
        forum = self.get_object()
        if self.request.user == forum.user:
            return True
        return False


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description']
    success_url = '/forum/'

    def form_valid(self, form):
        _forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.forum = _forum
        return super().form_valid(form)
