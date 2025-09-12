from django.shortcuts import get_object_or_404, render, redirect
from book.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from book.form import CategoryForm, CustomUserCreationForm, BookForm
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.

@login_required
def profile_view(request):
    return render(request, 'account/profile.html', {'user': request.user})

@login_required
def home_page(request):
    logged_in_flag = request.GET.get("logged_in", None)
    return render(request, "base_generic.html", {
        "logged_in_flag": logged_in_flag
    })

@login_required
def book_list(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    if query:
        books = books.filter(
            models.Q(title__icontains=query) |
            models.Q(authors__first_name__icontains=query) |
            models.Q(authors__last_name__icontains=query)
        ).distinct()

    if category_id and category_id != 'all':
        books = books.filter(categories__id=category_id)

    user_favorites = Favorite.objects.filter(user=request.user).values_list('book_id', flat=True)
    categories = Category.objects.all()

    return render(request, 'books/book_list.html', {
        'book_list': books,
        'favorite_ids': list(user_favorites),
        'categories': categories,
        'selected_category': category_id or 'all',
        'query': query or '',
    })




@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') 
    else:
        form = CategoryForm()
    return render(request, 'books/add_category.html', {'form': form})



def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})


@login_required
def toggle_favorite(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, book=book)
        if not created:
            favorite.delete()
            is_favorite = False
        else:
            is_favorite = True
        return JsonResponse({'success': True, 'is_favorite': is_favorite})
    return JsonResponse({'success': False})

@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('book')
    return render(request, 'account/my_favorites.html', {'favorites': favorites})



def logout_view(request):
    logout(request)
    return redirect('account/login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, 'account/form.html', {
                'error': "Invalid username or password",
                'title': 'Login',
                'button_text': 'Login'
            })
    return render(request, 'account/form.html', {
        'title': 'Login',
        'button_text': 'Login'
    })


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/form.html', {
        'form': form,
        'title': 'Register',
        'button_text': 'Register'
    })



