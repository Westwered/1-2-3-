from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'core/register.html', {'form': form})

@login_required
def order_certificate(request):
    if request.method == 'POST':
        return redirect('order_success')
    return render(request, 'core/order.html')

def order_success(request):
    return render(request, 'core/order_success.html')