from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import translation

def show(request):
	context = {}
	return render(request, 'core_home/show.html', context=context)
