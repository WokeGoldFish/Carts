from distutils.command.clean import clean
from multiprocessing import context
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import PostForm, CreateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def homePg(request):
    posts = Post.objects.all()
    context= {'posts': posts}
    return render(request, 'ecom/homepage.html', context=context)




def signIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        
        user = authenticate(request , username=username, password=password1)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'{username} is now signed in!')
            return redirect('home')
        else:
            messages.warning(request, f'Login Information is incorrect')
            
    
    return render(request, 'ecom/signin.html', context = {})

def signUp(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, f'Account Created {user}!')
            return redirect('signin')
        else:
            messages.warning(request, f'Invalid Attempt')
            print('invalid', form.errors)
    else:
        print('get req submitted', request.method)            
        
    return render(request, 'ecom/signup.html', context = {'form':form})


def logOut(request):
    logout(request)
    return redirect('signin')


def singlePost(request, post_id):
    post = Post.objects.get(id=post_id)
    
    
    return render(request, 'ecom/post.html', context = {'p': post})

# @login_required
# def addToCart(request, post_id):
#     post = Post.objects.get(id=post_id)
#     if request.method == 'POST':
#         if post.is_valid():
#             post.save()
#             messages.success(request, 'You have successfully added this item to your cart')
#             return redirect('home') 
#     return render(request, 'ecom/cart.html', context = {'p':post})

# c = Cart -- instantiate a cart item
# c.user_id = request.user.id
# c.product_id = post_id
    #c.save()



def addToCart(request, post_id):
    # try:
    post = Post.objects.get(id = post_id)  
    join = Cart()
    join.customer = request.user
    join.product = post
    join.save()
    
    return redirect('home')