from django.urls import path
from . import views


urlpatterns = [

    path('IncomeIndex', views.IncomeView, name="income_url"),
    path('add-income', views.add_incomeView, name="add-income_url"),
    path('edit-income/<int:id>', views.income_editView, name="income-edit_url"),
    path('income-delete/<int:id>', views.delete_incomeView, name="income-delete_url"),
    path('add-source/', views.AddSourceView, name='add-source_url'),

    path('search-income', views.ShowResultsView, name='show_results'),
    ]

