from django import forms
from django.forms import fields

from .models import PostModel

class AddPostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields= ('text',)

    def __init__(self,*args,**kwargs):
        super(AddPostForm,self).__init__(*args,**kwargs)

        self.fields['text'].widget.attrs = {'class':'form-control bg-dark opacity-75 text-white','rows':'11'}


class EditPostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields= ('text',)

    def __init__(self,*args,**kwargs):
        super(EditPostForm,self).__init__(*args,**kwargs)
        self.fields['text'].widget.attrs = {'class':'form-control bg-dark opacity-75 text-white','rows':'11'}
