from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('expenseindex/', views.Expenseindex, name='expense_url'),
    path('add-expense', views.ExpenseAdd, name="add-expense_url"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('add-category/', views.AddCategoryView, name='add-category_url'),
    path('search-expense', views.ExpenseResultsView, name='show_expense'),
    ]

