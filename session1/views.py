from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from session1.forms import SignUpForm

# Create your views here.
def cookiex(request):
    if 'visit' in request.COOKIES:
        count = int(request.COOKIES['visit']) + 1
    else:
        count = 1
    response = render(request, 'session1/session1.html', {'count': count})
    response.set_cookie('visit', count)
    return response

def signup(request):
    pass

def signup(request):

    if request.method == 'POST':
        print("POST..")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            user.set_password(user.password)

            return redirect('/fview/show/')
    else:
        form = SignUpForm()
        print('here')
    return render(request, 'registration/signup.html', {'form': form})
