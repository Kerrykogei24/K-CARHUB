from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url="/accounts/login/")
def index(request):
    return render(request,'index.html')





def signUp(request):    
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['username']
            email = form.cleaned_data['email']
            send=welcome_email(name,email)
            HttpResponseRedirect('home')
    else:
        form = SignUpForm()
    return render(request,'registration/registration_form.html',{'form':form})


@login_required(login_url="/accounts/login/")
def logout_request(request):
    logout(request)
    return redirect('home')

def profile(request, username):
    title = 'Creative || Hub'
    profile = User.objects.get(username=username)
    users = User.objects.get(username=username)
    follow = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    people_following = Follow.objects.following(request.user)
    
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
        
    return render(request, 'profile.html', {'title': title, 'following':following, 'follow':follow, 'users':users, 'people_following':people_following, 'profile_details':profile_details})
