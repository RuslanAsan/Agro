from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from income.helpers import calculate_income_total, add_income_items_to_warehouse
from income.models import Income, IncomeItem
from order.helpers import contr_agent_balance_income, contr_agent_balance_outcome
from payment.choices import PAYMENT_TYPE_CHOICES, PAYMENT_METHOD_CHOICES
from payment.helpers import payment_outcome
from payment.models import ProjectSetting, PaymentLog
from product.models import Product


class ProductView(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')


class ProductCreate(CreateView):
    template_name = 'product_create.html'
    model = Product
    fields = ['title', 'size', 'price', 'status', 'code']
    success_url = '/'


class ProductUpdate(UpdateView):
    template_name = 'product_udate.html'
    model = Product
    fields = ['title', 'size', 'price', 'status', 'code']
    success_url = '/'

