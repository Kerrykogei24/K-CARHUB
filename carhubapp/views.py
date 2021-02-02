from django.shortcuts import render

# Create your views here.

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
            HttpResponseRedirect('pics')
    else:
        form = SignUpForm()
    return render(request,'registration/registration_form.html',{'form':form})


@login_required(login_url="/accounts/login/")
def logout_request(request):
    logout(request)
    return redirect('pics')
