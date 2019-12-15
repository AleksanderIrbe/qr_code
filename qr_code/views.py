from django.http import HttpResponse
from django.shortcuts import redirect, render


# для стартовой страницы
def hello(request):
	return render(request, 'qr_list/qr_hello.html')

def view404(request, exception='Page not Found'):
	return render(request, 'errs/404.html')
