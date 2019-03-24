from django.shortcuts import render, redirect,Http404,HttpResponse
from .forms import UserForm, BookProduct
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import BookList
from django.contrib.auth.models import User

# Create your views here.

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('user')
    else:
        context = {
            'form': form,
        }
        return render(request, 'accounts/register.html', context)


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            # if user.is_active:
            # user = user.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('user'))
            # return redirect('user')
            # else:
            # return render(request, 'accounts/user.html', {'error_message': 'Your account has been disabled'})
        else:
            context['error'] = 'Invalid'
            return render(request, 'accounts/login.html', context)  # ,{'error_message': 'Invalid login'})
    else:
        return render(request, 'accounts/login.html', context)


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('login'))

    # logout(request)
    # form = UserForm(request.POST or None)
    # context = {
    # "form": form,
    # }


# return render(request, 'accounts/index.html', context)


def index(request):                 #Main Homepage
    context = {}
    books = BookList.objects.all()
    context['books'] = books
    context['user'] = request.user
    return render(request, 'accounts/index.html', context)


def user_view(request):            #User Homepage After Login
    context = {}
    books = BookList.objects.all()
    context['books'] = books
    context['user'] = request.user
    return render(request, 'accounts/user.html', context)


def profile_view(request):
    args = {'user': request.user}
    return render(request, 'accounts/book_list.html',args)


def book_form(request):
    book = BookList.objects.all()
    return render(request, 'accounts/book_list.html', {'book': book})


def book_create(request):
    form = BookProduct(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)

        instance.save()
        return redirect('list')

    context = {
        'form': form,
    }
    return render(request, 'accounts/add_book.html', context)


def update_view(request, id):
    book = BookList.objects.get(id=id)
    form = BookProduct(request.POST or None, request.FILES or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('list')

    context = {
        'form': form,
    }
    return render(request, 'accounts/add_book.html', context)


def delete_view(request, id):
    book = BookList.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('list')

    return render(request, 'accounts/delete_list.html', {'book': book})


def book_details(request, id=None):
    context={}
    book = BookList.objects.get(id=id)
    context['book'] = book
    return render(request,'accounts/book_detail.html', context)
