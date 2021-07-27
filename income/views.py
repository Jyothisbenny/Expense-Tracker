from django.shortcuts import render, redirect
from income.models import UserIncome, Source
from django.contrib.auth.decorators import login_required
from pyexpat.errors import messages
from django.core.paginator import Paginator


# Create your views here.

@login_required(login_url='/accounts/login_url')
def IncomeView(request):
    sources = Source.objects.all()
    income = UserIncome.objects.filter(owner=request.user)
    paginator = Paginator(income, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    # currency = UserPreference.objects.get(user=request.user).currency
    context = {
        'income': income,
        'page_obj': page_obj,
        # 'currency': currency
    }
    return render(request, 'income/index.html', context)


@login_required(login_url='/accounts/login_url')
def add_incomeView(request):
    sources = Source.objects.filter(owner=request.user)
    context = {
        'sources': sources,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'income/add_income.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/add_income.html', context)
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'income/add_income.html', context)

        UserIncome.objects.create(owner=request.user, amount=amount, date=date,
                                  source=source, description=description)
        # messages.success(request, 'Record saved successfully')

        return redirect('income_url')


# @login_required(login_url='/authentication/login')
def income_editView(request, id):
    income = UserIncome.objects.get(pk=id)
    sources = Source.objects.filter(owner=request.user)
    context = {
        'income': income,
        'values': income,
        'sources': sources,
    }
    if request.method == 'GET':
        return render(request, 'income/edit_income.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/edit_income.html', context)
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'income/edit_income.html', context)
        income.amount = amount
        income.date = date
        income.source = source
        income.description = description

        income.save()
        # messages.success(request, 'Record updated  successfully')

        return redirect('income_url')


def delete_incomeView(request, id):
    income = UserIncome.objects.get(pk=id)
    income.delete()
    # messages.success(request, 'record removed')
    return redirect('income_url')


def AddSourceView(request):
    if request.method == 'POST':
        name = request.POST['Source_name']
        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'income/add_Source.html')

        Source.objects.create(owner=request.user, name=name)
        # messages.success(request, 'Source saved successfully')

        return redirect('add-source_url')
    else:
        return render(request, 'income/add-Source.html')


def ShowResultsView(request):
    if request.method == "POST":
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        SearchResults = UserIncome.objects.filter(owner=request.user, date__gte=start_date, date__lte=end_date)
        paginator = Paginator(SearchResults, 5)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        context = {
            'income': SearchResults,
            'page_obj': page_obj,

        }
        return render(request, 'income/searchincome.html', context)
    else:
        return render(request, 'income/searchincome.html')
