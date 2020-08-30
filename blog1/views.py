from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentsForm
from .models import Post, Comments
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
# Create your views here.


class AboutView(TemplateView):
    template_name = 'blog1/about.html'

class PostCreateView(CreateView):
    form_class = PostForm

    model = Post

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    form_class = PostForm
    
    model = Post

class PostListView(ListView):
    model = Post

    # queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


    
class PostDeleteView(DeleteView):
    model = Post
    
    success_url = reverse_lazy('list')

class PostDraftView(ListView):
    model = Post

    queryset = Post.objects.filter(published_date__isnull=True).order_by('-created_date')


class CommentCreateView(CreateView):
    form_class = CommentsForm

    model = Comments

    def form_valid(self,form):
        form.instance.post = Post.objects.filter(pk=self.kwargs['pk'])[0]
        form.instance.author = self.request.user
        return super().form_valid(form)

class ApproveView(View):

    def get(self,request,pk):
        comment = get_object_or_404(Comments,pk=pk)
        comment.approve_comment()
        return redirect('detail',pk=comment.post.pk)

class CommentDelete(View):

    def get(self,request,pk):
        comment = get_object_or_404(Comments,pk=pk)
        post_pk = comment.post.pk
        comment.delete()
        return redirect('detail',pk=post_pk)

class PublishView(View):

    def get(self,request,pk):
        post = get_object_or_404(Post,pk=pk)
        post.publish()
        return redirect('list')
