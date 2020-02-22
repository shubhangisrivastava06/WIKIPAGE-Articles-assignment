from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from reportlab.pdfgen import canvas
from .models import User
from .models import Articles
from .forms import LoginForm, RegisterForm, AddArticleform, GuestinfoForm


def login(request):
    if request.session.get('email'):
        return redirect('submit')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        abc = User.objects.filter(email=email, password=password)

        if abc:
            request.session['email'] = email
            return redirect('submit')
        else:
            print('not match')

    context = {
        'form': form
    }
    return render(request, 'Users/login.html', context)


def signup(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'Users/signup.html', context)


def submit(request):
    if not request.session.get('email'):
        return redirect('login')
    se_email = request.session.get('email')

    login_user = User.objects.get(email=se_email)

    form = AddArticleform(request.POST or None, request.FILES or None)
    if form.is_valid():
        Section = form.cleaned_data.get('Section')
        SubSection = form.cleaned_data.get('SubSection')
        title = form.cleaned_data.get('title')
        article = form.cleaned_data.get('article')

        submissions = Articles(user=login_user, Section=Section, SubSection=SubSection, title=title, article=article)
        submissions.save()

    context = {
        'form': form,
        'login_user': login_user,

    }
    return render(request, 'Users/submit.html', context)


def logout(request):
    del request.session['email']
    return redirect('allarticles')


def all_articles(request):
    user = None

    posts = Articles.objects

    if request.session.get('email'):
        user = request.session.get('email')

    context = {
        'posts': posts,
        'user': user
    }
    return render(request, 'Users/wikipage.html', context)


def detail(request, post_id):
    detailarticle = get_object_or_404(Articles, pk=post_id)
    return render(request, 'Users/wikipage.html', {'post': detailarticle})


def Guestinfo(request):
    form = GuestinfoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'Users/Guestinfo.html', context)
