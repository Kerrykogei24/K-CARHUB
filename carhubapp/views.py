from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from . models import Post, Profile, Comments
from . forms import PostComments, PostImagesForm,PostProfile, UpdateUserProfileForm, NewsLetterForm,SignUpForm
from friendship.models import Friend, Follow, Block
from friendship.exceptions import AlreadyExistsError
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.

@login_required(login_url = '/accounts/login/')
def index(request):
    title = 'Car || Hub'
    return render(request, 'landing/index.html',{'title': title})


def about(request):
    title = 'Car || Hub'
    form = NewsLetterForm()
    
    return render(request, 'about.html',{'title': title, 'form': form})
    
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


def photos(request):
    title = 'Car || Hub'
    posts = Post.objects.all()
    form = NewsLetterForm()
    return render(request,'photo.html',{'posts':posts , 'title':title, 'form':form})



def post_image(request):
    title = 'Car|| Hub'
    if request.method == 'POST':
        form = PostImagesForm(request.POST,request.FILES) 
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(photos)
            
    else:
        form = PostImagesForm()
        print('method is not post')
        
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None
    return render(request,'post_image.html',{'posts': posts, 'form':form, 'title':title})




def logout_request(request):
    logout(request)
    return redirect('/accounts/login/')

def profile(request, username):
    title = ' Car || Hub'
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

def edit_profile(request, username):
    title = 'Car || Hub'
    user = User.objects.get(username=username)
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            
            prof_form.save()
            return redirect('profile', user.username)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'prof_form': prof_form,
        'title': title
    }
    return render(request, 'edit.html', params)



def single_car(request, art_id): 
    title = 'Car || Hub'
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
            return redirect('single-car', art_id = art_id )
        
    else:
        form = PostComments()
    return render(request, 'single_car.html', {'arts':arts,'form':form, 'comments':comments, 'title':title})


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



class FlashcardDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = ('/')

def deleteForm(request):
    context ={     
    }
    return render(request ,'delete.html', context )   