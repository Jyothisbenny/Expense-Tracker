from django.shortcuts import render, redirect
from .models import Category, Expense
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def Expenseindex(request):
    categories = Category.objects.filter(owner=request.user)
    expenses = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
        'expenses': expenses,
        'page_obj': page_obj,

    }
    return render(request, 'expenses/index.html', context)


def ExpenseAdd(request):
    categories = Category.objects.filter(owner=request.user)
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/add_expense.html', context)
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'expenses/add_expense.html', context)

        Expense.objects.create(owner=request.user, amount=amount, date=date,
                               category=category, description=description)
        messages.success(request, 'Expense saved successfully')

        return redirect('expense_url')


def expense_edit(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.filter(owner=request.user)
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories
    }
    if request.method == 'GET':
        return render(request, 'expenses/edit-expense.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/edit-expense.html', context)
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'expenses/edit-expense.html', context)

        expense.owner = request.user
        expense.amount = amount
        expense.date = date
        expense.category = category
        expense.description = description

        expense.save()
        messages.success(request, 'Expense updated  successfully')

        return redirect('expense_url')


def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Expense removed')
    return redirect('expense_url')


def AddCategoryView(request):
    if request.method == 'POST':
        name = request.POST['Category_name']
        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'expenses/add_Category.html')

        Category.objects.create(owner=request.user, name=name)
        messages.success(request, 'Category saved successfully')

        return redirect('add-category_url')
    else:
        return render(request, 'expenses/add-Category.html')


def ExpenseResultsView(request):
    if request.method == "POST":
        start_date = request.POST.get('start_date1')
        end_date = request.POST.get('end_date1')
        SearchResults = Expense.objects.filter(owner=request.user, date__gte=start_date, date__lte=end_date)
        paginator = Paginator(SearchResults, 5)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context = {
            'expense': SearchResults,
            'page_obj': page_obj,
                    }
        return render(request, 'expenses/searchexpense.html', context)
    else:
        return render(request, 'expenses/searchexpense.html')