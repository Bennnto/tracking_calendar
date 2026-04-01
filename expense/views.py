from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ExpenseForm
from .models import Expense


def list_expense(request):
    expenses = Expense.objects.all().values()
    template = loader.get_template('expense.html')
    context = { 'form': ExpenseForm(), 'expenses': expenses }
    return HttpResponse(template.render(context, request))

def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('expense')
    else :
        form = ExpenseForm()
    expenses = Expense.objects.all().values()
    template = loader.get_template('expense.html')
    context = { 'form': form, 'expenses': expenses }
    return HttpResponse(template.render(context, request))

def delete_expense(request, id):
    content = get_object_or_404(Expense, id = id)
    content.delete()
    return redirect('expense')     


        