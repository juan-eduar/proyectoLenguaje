from django.shortcuts import render, redirect, get_object_or_404

from .models import *

from .form import UserRegisterForm, PostForm

from django.contrib.auth.models import User

from django.contrib import messages





# Create your views here.

def feed(request):
  
  post = Post.objects.all()

  context = {'post': post}	

  return render(request,'social/feed.html', context)

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      messages.success(request, f'Usuario {username} creado')
      return redirect('feed')
  else:
    form = UserRegisterForm()

  context = { 'form' : form }
  return render(request, 'social/register.html', context)






  



def profile(request, username=None):

 current_user = request.user

 if username and username != current_user.username:

  user = User.objects.get(username=username)

  post = user.post.all()
 
 else:

  post = current_user.post.all()

  user = current_user


 
 return render(request,'social/profile.html', {'user': user, 'post': post})


def post(request):

 current_user = get_object_or_404(User, pk=request.user.pk)

 if  request.method == 'POST':

   form = PostForm(request.POST)

   if form.is_valid():

    post = form.save(commit=False)

    post.user = current_user

    post.save()

    messages.success(request,f'Post creado ')

    return redirect('feed')
 
 else:

  form = PostForm()

 return render(request, 'social/Post.html', {'form': form})





 