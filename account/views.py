from django.http import HttpResponseRedirect, request
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View,DeleteView
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.http import JsonResponse
from django.views.generic.list import ListView
from .mixins import ChangeProfileMixins
from Post.models import PostModel
from .models import BlockAndReportModel, RelationModel, User
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

from .forms import LoginUserForm,RegisterUserForm,ProfileForm,BlockUseForm,ReportUserForm
# Create your views here.


class LoginUserView(LoginView):
    template_name = "auth/login.html"
    form_class = LoginUserForm
    success_message = "You Logined successfully"

    def get_success_url(self):
        return reverse_lazy('post:List')


class RegisterUserView(CreateView):
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')
    form_class = RegisterUserForm
    success_message = "Your profile was created successfully"


class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')



class PassResetView(PasswordResetView):
    template_name = 'auth/password_reset/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'auth/password_reset/password_reset_email.html'


class PassResetDoneView(PasswordResetDoneView):
   template_name = 'auth/password_reset/password_reset_done.html'


class PassResetConfirm(PasswordResetConfirmView):
    template_name = 'auth/password_reset/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')

class PassResetComplete(PasswordResetCompleteView):
    template_name = 'auth/password_reset/password_reset_complete.html'





class ProfileView(ChangeProfileMixins,LoginRequiredMixin,UpdateView):
    template_name = 'auth/profile.html'
    success_url = '/'
    form_class = ProfileForm




    def get_object(self):
        global user
        username = self.kwargs.get('username')
        user =  get_object_or_404(User,username = username)
        return user

    def get_context_data(self,**kwargs):
        post = PostModel.objects.filter(user = user)
        context = super().get_context_data(**kwargs)
        context['post'] = post


        is_following = False
        relation = RelationModel.objects.filter(from_user = self.request.user,to_user = user )
        if relation.exists():
            is_following = True

        context['is_following'] = is_following
        return context


class BlockUserView(View):
    template_name = 'auth/block.html'
    
    def get(self,*args,**kwargs):
        username = self.kwargs.get('username')
        user_blocked = get_object_or_404(User,username = username)
        for x in self.request.user.blocked_users.all():
            if x == user_blocked:
                raise Http404('you bocked this user ')

            else:
                pass
        add_user = User.objects.get(username = user_blocked)
        self.request.user.blocked_users.add(add_user)
        messages.success(self.request,f"You Blocked '{ username }' successfuly")
        return redirect('post:List')



class ReportUserView(CreateView):
    template_name = 'auth/report.html'
    form_class = ReportUserForm
    
    def form_valid(self, form):

        #user reported
        username = self.kwargs.get('username')
        user = get_object_or_404(User,username = username)

        #post reported
        post = self.kwargs.get('text')
        post_reported = get_object_or_404(PostModel,text = post)
 
        my_form = form.save(commit = False)
        my_form.reporter = self.request.user
        my_form.reported = user
        my_form.report_on_post = post_reported
        my_form.number_reported = 1
        my_form.save()

        return redirect('post:List')



@login_required
def follow(request):
	if request.method == 'POST':
		user_id = request.POST['user_id']
		following = get_object_or_404(User, pk=user_id)
		check_relation = RelationModel.objects.filter(from_user=request.user, to_user=following)
		if check_relation.exists():
			return JsonResponse({'status':'exists'})
		else:
			RelationModel(from_user=request.user, to_user=following).save()
			return JsonResponse({'status':'ok'})


@login_required
def unfollow(request):
	if request.method == 'POST':
		user_id = request.POST['user_id']
		following = get_object_or_404(User, pk=user_id)
		check_relation = RelationModel.objects.filter(from_user=request.user, to_user=following)
		if check_relation.exists():
			check_relation.delete()
			return JsonResponse({'status':'ok'})
		else:
			return JsonResponse({'status':'notexists'})
