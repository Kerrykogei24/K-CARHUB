from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from . models import Post, Profile, Comments
from . forms import PostComments, PostImagesForm,PostProfile, UpdateUserProfileForm, NewsLetterForm
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from friendship.exceptions import AlreadyExistsError


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
    title = 'K CAR || Hub'
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



def single_car(request, art_id): 
    title = 'Creative || Hub'
    arts = Post.objects.get(id=art_id)
    comments = Comments.get_comment_by_image(id = art_id)
    
    current_user = request.user
    if request.method == 'POST':
        form = PostComments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.arts = arts
            comment.user = request.user
            comment.save()
            return redirect('single-art', art_id = art_id )
        
    else:
        form = PostComments()
    return render(request, 'single_art.html', {'arts':arts,'form':form, 'comments':comments, 'title':title})


def follow(request, user_id):
    other_user = User.objects.get(id=user_id)
    follow = Follow.objects.add_follower(request.user, other_user)

    return redirect('single-car')

@login_required(login_url='/accounts/login/')
def unfollow(request, user_id):
    other_user = User.objects.get(id=user_id)

    follow = Follow.objects.remove_follower(request.user, other_user)

    return redirect('single-car')


def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')
    
    recipient = NewsLetterRecipients(name = name, email = email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)


