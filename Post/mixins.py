from django.shortcuts import redirect

class SearchPremissionMixin:
    def dispatch(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request,*args,**kwargs)
        else:
            return redirect('post:List')


class LoginOrListMixin:
    def dispatch(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request,*args,**kwargs)
        else:
            return redirect('post:List')

