from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import LostItemForm, ClaimForm
from .models import LostItem, Claim
# Create your views here.

def home(request):
    return render(request, "home.html")

def profile_view(request):
    return render(request, 'registration/profiles.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
        
    return render(request, 'registration/login.html')

class ReportView(LoginRequiredMixin, CreateView):
    model = LostItem
    form_class = LostItemForm
    template_name = 'report.html'
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Assign logged-in user
        return super().form_valid(form)
    
class ItemsView(ListView):
    model = LostItem
    template_name = 'items.html'
    context_object_name = 'items'

class DetailView(DetailView):
    model = LostItem
    template_name = 'detail.html'
    context_object_name = 'item'

class DeleteView(DeleteView):
    model = LostItem
    template_name = 'delete.html'
    success_url = reverse_lazy('items')

class UpdateView(UpdateView):
    model = LostItem
    form_class = LostItemForm
    template_name = 'update.html'
    success_url = reverse_lazy('items')

def claim_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)

    # Check if user has already claimed this item
    existing_claim = Claim.objects.filter(item=item, claimed_by=request.user).exists()
    if existing_claim:
        messages.error(request, "You have already claimed this item!")
        return redirect('items')

    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.item = item
            claim.claimed_by = request.user
            claim.save()
            messages.success(request, "Your claim request has been submitted!")
            return redirect('items')
    else:
        form = ClaimForm()

    return render(request, 'claim.html', {'form': form, 'item': item})
