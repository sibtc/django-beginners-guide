from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import SignUpForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy

# Create your views here.
 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

@method_decorator(login_required, name='dispatch')    
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name='my_account.html'
    success_url = reverse_lazy('my_account')
    
    def get_object(self):
        return self.request.user