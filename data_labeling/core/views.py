from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, DataUploadForm, AnnotationForm
from .models import Data, Annotation

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
            pending_tasks = Data.objects.filter(status='pending')
            return render(request, 'annotator_home.html', {'pending_tasks': pending_tasks})
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

@login_required
def annotate_task_view(request, task_id):
    if request.user.role != 'annotator':
        return redirect('home')

    data_task = get_object_or_404(Data, id=task_id)

    if request.method == 'POST':
        form = AnnotationForm(request.POST)
        if form.is_valid():
            annotation = form.save(commit=False)
            annotation.annotator = request.user
            annotation.data = data_task
            annotation.status = 'approved' if 'approve' in request.POST else 'rejected'
            annotation.save()

            data_task.status = 'review'
            data_task.save()

            return redirect('annotator_home')
    else:
        form = AnnotationForm()

    return render(request, 'annotate_task.html', {'data_task': data_task, 'form': form})