from django.http import HttpResponse
from django.shortcuts import redirect, render

# для стартовой страницы
def hello(request):
	return render(request, 'qr_list/qr_hello.html')


