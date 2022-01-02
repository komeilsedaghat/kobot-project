from datetime import timedelta
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import fields, widgets
from .models import User,BlockAndReportModel

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields= ('username','password',)

    def __init__(self,*args,**kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Username or Email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'})



class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2','age','phone_number',)

    
    def __init__(self,*args,**kwargs):
        super(RegisterUserForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Your Username"
        self.fields['email'].widget.attrs['placeholder'] = "Your Email"
        self.fields['age'].widget.attrs['placeholder'] = 'Your Age'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Your Phone Number'
        self.fields['password1'].widget.attrs['placeholder'] = 'Your Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Your Confirm Password'


    

    def clean_password2(self):
        p2 = self.cleaned_data['password2']
        p1 = self.cleaned_data['password1']
        if p2 != p1:
            raise forms.ValidationError('password not match')
        else:
            None


        if len(p2) < 5 :
            raise forms.ValidationError('you password is too short')
        else:
            None

        


    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name",)

    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['first_name'].widget.attrs['class'] = "form-control"
        self.fields['last_name'].widget.attrs['class'] = "form-control"
        
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     user  = User.objects.get(username = username)
    #     delta_time = timedelta(days=30)
    #     if user.last_profile_updated > delta_time:
    #         return self.clean()
    #     else:
    #         raise forms.ValidationError('you changed your username less then 30 days ago ')


class BlockUseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('blocked_users',)


    blocked_users = forms.ModelMultipleChoiceField(
    queryset=User.objects.all(),
    widget=forms.CheckboxSelectMultiple
    )

    

class ReportUserForm(forms.ModelForm):
    class Meta:
        model = BlockAndReportModel
        fields = ('report_text',)
