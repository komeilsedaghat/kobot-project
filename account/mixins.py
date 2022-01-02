from datetime import datetime, time, timedelta, tzinfo
from django.http.response import Http404
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect

class ChangeProfileMixins:
    def form_valid(self,form):
        user_change = form.save(commit = False)
        user = self.request.user

        if user.is_premium_account:
            user.last_profile_updated = timezone.now
            user_change.save()
        else:
            last = user.last_profile_updated
            now  = datetime.now()
            subtract_time = now - last.replace(tzinfo=None) 
            if subtract_time > timedelta(days=30):
                user.last_profile_updated = timezone.now
                user_change.save()
            else:
                raise Http404('your account is not premium')

        url = reverse_lazy('post:List')
        return HttpResponseRedirect(url)



