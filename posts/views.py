from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Home page - shows all notes
@login_required
def home(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'posts/home.html', {'notes': notes})

# Create note page
@login_required
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content, author=request.user)
        return redirect('home')
    return render(request, 'posts/create_note.html')

# Edit note page
@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('home')
    return render(request, 'posts/edit_note.html', {'note': note})

# Delete note
@login_required
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id, author=request.user)
    note.delete()
    return redirect('home')

# Login page
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('login')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('home')
            messages.error(request, "Wrong Password")
            return redirect('login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('register')
    return render(request, "posts/login.html")

# Register page
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('register')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('register')
    return render(request, "posts/register.html")

# Logout function
def custom_logout(request):
    logout(request)
    return redirect('login')
