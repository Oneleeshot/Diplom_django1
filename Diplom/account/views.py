from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.template.context_processors import csrf


def register_user(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.method == 'POST':
        new_form = UserCreationForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            new_user = auth.authenticate(
                username=new_form.cleaned_data['username'],
                password=new_form.cleaned_data['password1'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            args['form'] = new_form
    return render(request, 'registration/register.html', context=args)
