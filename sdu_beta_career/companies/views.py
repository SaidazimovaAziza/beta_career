from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Company

from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def company_list(request):
    companies = Company.objects.filter()

    return render(request, 'company_list.html', {'companies': companies})


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company_detail.html', {'company': company})


