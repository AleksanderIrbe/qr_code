from django.http import HttpResponse
from django.shortcuts import redirect, render


# для стартовой страницы
def hello(request):
	return render(request, 'qr_list/qr_hello.html')


# для страниц с ошибками
def view403(request, exception='HTTP Forbidden'):
	return render(request, 'errs/403.html')

def view404(request, exception='Page not Found'):
	return render(request, 'errs/404.html')

def view500(request, exception=None):
	return render(request, 'errs/500.html')
