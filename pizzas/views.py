from django.shortcuts import render
from .models import Pizza

def home(request):
    return render(request, 'pizzas/home.html')


def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas':pizzas
    }
    return render(request, 'pizzas/pizzas.html', context)


from .forms import PizzaForm
from django.shortcuts import redirect
from django.contrib import messages


def order(request, id):
    pizza = Pizza.objects.get(id=id)
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
            order.user = request.user
            order.save()
            messages.success(request, 'Order is on the way!!')
            return redirect('home')
    context = {
        'pizza': pizza,
        'form': form,
    }
    return render(request, 'pizzas/order.html', context)