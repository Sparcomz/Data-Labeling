from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, DataUploadForm
from .models import Data

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def home_view(request):
    if request.user.is_authenticated:
        user = request.user
        if user.role == 'uploader':
            uploaded_data = Data.objects.filter(uploader=user)
            return render(request, 'uploader_home.html', {'uploaded_data': uploaded_data})
        elif user.role == 'annotator':
            return render(request, 'annotator_home.html')
        elif user.role == 'reviewer':
            return render(request, 'reviewer_home.html')
        elif user.role == 'admin':
            return render(request, 'admin_home.html')
    return render(request, 'home.html')

@login_required
def upload_data_view(request):
    if request.user.role != 'uploader':
        return redirect('home')

    if request.method == 'POST':
        form = DataUploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.uploader = request.user
            data.status = 'pending'
            if 'image_file' in request.FILES:
                data.image_content = request.FILES['image_file'].read()  # Read file as binary
            data.save()
            return redirect('uploader_home')
    else:
        form = DataUploadForm()

    return render(request, 'upload_data.html', {'form': form})