from django.views.generic import ListView,CreateView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from account.models import RelationFollowingModel
from .forms import AddPostForm,EditPostForm,CommentForm
from django.db.models import Q
from .mixins import SearchPremissionMixin
from .models import CommentsModel, PostModel
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.



class ListAddPostView(LoginRequiredMixin,ListView):
    template_name = "Post/list.html"
    form_class = AddPostForm
    paginate_by = 2


    def post(self,request,*args,**kwargs):
        form = self.form_class()
        my_form = form.save(commit=False)
        my_form.user = self.request.user

        text_form =self.request.POST.get('text')
        print(text_form)
        my_form.text = text_form

        try:
            file = self.request.FILES['file']
            print(file.content_type)
            if file.content_type[:5] == 'image':
                my_form.image = file
                my_form.save() 
            elif file.content_type[:5] == 'video':
                my_form.video = file
                my_form.save() 
            elif file.content_type[:5] == 'audio':
                my_form.audio = file
                my_form.save()
       
            else:
                messages.error(self.request,"Your uploaded file most be video or photo")
                      
        except:
            my_form.save()

        
        return HttpResponseRedirect('/')

        
    

    def get_queryset(self):
        if self.request.user.blocked_users.exists():
            block = PostModel.objects.exclude(Q(user__in = self.request.user.blocked_users.all())|Q(status = False))
        else:
            block = PostModel.objects.filter(status = True)
        return block
    



    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = AddPostForm()
        #follower
        follower = RelationFollowingModel.objects.filter(to_user = self.request.user).count()
        context['follower'] = follower

        #post
        count_post = PostModel.objects.filter(user = self.request.user).count()
        context['count_post'] = count_post

        return context



    
    
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


