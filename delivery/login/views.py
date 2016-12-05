from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import UserForm, GroupForm
from django.template import RequestContext
import sys
from django.contrib.auth.models import Group

def login(request, next):
    authenticated = False
    redirect_to = next
    login_error = None

    if request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username, ' ', password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            authenticated = True
        else:
            login_error = "User not found"

    else:
        user_form = UserForm()
        group_form = GroupForm()

    if authenticated:
        auth.login(request, user)
        return redirect(redirect_to)
    else:
        return render(request, 'login.html', {'login_error': login_error, 'user_form': UserForm(), \
                                                 'group_form': GroupForm(), 'redirect_to' : 'homepage'})

def logout(request, next):
    auth.logout(request)
    redirect_to = next
    return redirect(redirect_to)  


def register(request, next):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
       
        user_form = UserForm(data=request.POST)
        group_form = GroupForm(data=request.POST)

        if user_form.is_valid() and group_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            group_name = GroupForm.GROUPS[int(group_form.cleaned_data['group'])] + 's'
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            user.save()
            registered = True
        else:
            pass
    else:
        user_form = UserForm()
        group_form = GroupForm()
    

    redirect_to = next
    if registered == False:
        return render(request, 'register.html', {'user_form': user_form, 'group_form': group_form, 'redirect_to' : 'homepage'})
    else:
        auth.login(request, user)
        return redirect(redirect_to)