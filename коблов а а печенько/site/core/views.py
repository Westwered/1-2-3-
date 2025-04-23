from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .forms import CertificateOrderForm

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
        form = CertificateOrderForm(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.save()
            return redirect('order_success')  # или куда тебе надо
    else:
        form = CertificateOrderForm()
    return render(request, 'core/order.html', {'form': form})

def order_success(request):
    return render(request, 'core/order_success.html')