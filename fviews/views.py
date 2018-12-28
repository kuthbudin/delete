from django.shortcuts import render, redirect
from fviews.forms import StudentRegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from fviews.models import RegistrationModel

# Create your views here.
def fview_test(request):
    return render(request, 'fviews/temp.html')

def registration(request):
    form = StudentRegistrationForm()
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            print("Valid")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            passw = form.cleaned_data['password']
            print(name, email)

            user = User.objects.create_user(name, email, passw)
            print("pww", passw)
            #user.set_password(passw)
            #print("pww2", user.password)

            return redirect('/fviews/show/')
            #return HttpResponse("<p>Success</p>")
        else:
            return render(request, 'fviews/reg.html', {'form': form})

    #return render(request, 'fviews/registration.html', {'form': form})
    return render(request, 'fviews/reg.html', {'form': form})

def showregistration(request):
    all_data = RegistrationModel.objects.all()
    print(all_data)
    #return HttpResponse("<h1>XYZ<h1>")
    return render(request, "fviews/show.html", {'all_data':all_data})
