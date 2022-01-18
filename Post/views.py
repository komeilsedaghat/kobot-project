from django.views.generic import ListView,CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from .forms import AddPostForm,EditPostForm,CommentForm
from django.db.models import Q
from .mixins import SearchPremissionMixin
from .models import CommentsModel, PostModel
from django.shortcuts import get_object_or_404, redirect,render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ListPostView(LoginRequiredMixin,ListView):
    paginate_by = 5
    
    template_name = "Post/list.html"


    def get_queryset(self):
        if self.request.user.blocked_users.exists():
            block = PostModel.objects.exclude(Q(user__in = self.request.user.blocked_users.all())|Q(status = False))
        else:
            block = PostModel.objects.filter(status = True)
        return block



        
class AddPostView(LoginRequiredMixin,CreateView):
    template_name = 'Post/add-post.html'
    form_class = AddPostForm
    

    def form_valid(self,form):
        x = form.save(commit = False)
        x.user = self.request.user
        x.save()
        url = reverse_lazy('post:List')
        return HttpResponseRedirect(url)
        
    
class EditPostView(LoginRequiredMixin,UpdateView):
    template_name = 'Post/edit-post.html'
    form_class = EditPostForm
    success_url = "/"

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        post = PostModel.objects.filter(pk = pk)
        return post
    

    
class SearchView(LoginRequiredMixin,SearchPremissionMixin,ListView):
    template_name = 'Post/search.html'

    def get_queryset(self):
        search = self.request.GET.get('search')

        if self.request.user.blocked_users.exists():
            for blocked_user in self.request.user.blocked_users.all():
                user = blocked_user
                all_post =  PostModel.objects.filter(Q(text__icontains = search))
                return all_post.exclude(Q(status = False)|Q(user = user.pk))
        else:
            return PostModel.objects.filter(Q(text__icontains = search))

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context



class CommentView(LoginRequiredMixin,CreateView):
    template_name = 'Post/comment.html'
    form_class = CommentForm

    def form_valid(self,form):
        my_form = form.save(commit = False)
        post_text = self.kwargs.get('text')
        post = PostModel.objects.get(text = post_text)
        my_form.post = post
        my_form.user = self.request.user
        my_form.save()
        return redirect('/')


    def get_context_data(self, **kwargs):
        post_text = self.kwargs.get('text')
        post = PostModel.objects.get(text = post_text)
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentsModel.objects.filter(post = post )
        return context


