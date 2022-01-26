from pyexpat import model
from django import forms
from django.forms import fields

from .models import PostModel,CommentsModel

class AddPostForm(forms.ModelForm):
 
    file = forms.FileField(required=False)

    class Meta:
        model = PostModel
        fields = ('text',)

    def __init__(self,*args,**kwargs):
        super(AddPostForm,self).__init__(*args,**kwargs)
        self.fields['text'].widget.attrs = {'class':'form-control','style':'height:35px;','placeholder':'Message...'}
        self.fields['file'].widget.attrs = {'class':'form-control','id':'file','style':' width:0.02px; height:15px;','hidden':''}

class EditPostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields= ('text',)

    def __init__(self,*args,**kwargs):
        super(EditPostForm,self).__init__(*args,**kwargs)
        self.fields['text'].widget.attrs = {'class':'form-control bg-dark opacity-75 text-white','rows':'11'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields= ('comment',)

    def __init__(self,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        self.fields['comment'].widget.attrs = {
            'class':'form-control bg-dark opacity-75 text-white ',
            'rows':'4',
            'placeholder':'write your comment'}
