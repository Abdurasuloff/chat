from django.shortcuts import render, get_object_or_404
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def profile(request, username):
    user=User.objects.get(username=username)
    is_owner = False
   
    if user==request.user:
         is_owner = True

    print(is_owner)        
    return render(request, 'profile.html', {"user":user})


class ProfileEditView(UpdateView):
    form_class = CustomUserChangeForm
    template_name = "edit-profile.html"
    def get_object(self):
        object = User.objects.get(username=self.kwargs.get("username"))
        return object
     
def discover(request):
    if 'q' in request.GET:
            q = request.GET['q']
            users = User.objects.filter(Q(username__icontains=q)|Q(first_name__icontains=q)| Q(last_name__icontains=q)).order_by("-last_login")
    else:
            users = User.objects.all().order_by('-last_login')

    return render(request, 'discover.html', {'users':users})