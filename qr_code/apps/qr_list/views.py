from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from . forms import ListForm
from . models import List
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse

# Create your views here.
# на главной странице для отображения таблицы
def base_page(request):
	latest_list = List.objects.all()
	admin_url = '../admin/qr_list/list/'
	return render(request, 'qr_list/qr_list.html', {'latest_list':latest_list, 'admin_url':admin_url,})
	

class ListDetail(View):
	def get(self, request, slug):
		detail = get_object_or_404(List, slug__iexact=slug)
		return render(request, 'qr_list/qr_detail.html', {'detail':detail})

class ListCreate(View):
	def get(self, request):
		form=ListForm()
		return render(request, 'qr_list/qr_create.html', {'form':form})

	def post(self, request):
		bound_form=ListForm(request.POST)
		if bound_form.is_valid():
			new_qr=bound_form.save()
			return redirect(new_qr)
		return render(request, 'qr_list/qr_create.html', {'form':bound_form})

		
class ListUpdate(View):
	def get(self, request, slug):
		detail = List.objects.get(slug__iexact=slug)
		bound_form = ListForm(instance=detail)
		return render(request, 'qr_list/qr_update.html', context={'form':bound_form, 'detail':detail})

	def post(self, request, slug):
		detail = List.objects.get(slug__iexact=slug)
		bound_form = ListForm(request.POST, instance=detail)
		if bound_form.is_valid():
			new_qr = bound_form.save()
			return redirect(new_qr)
		return render(request, 'qr_list/qr_update.html', context={'form':bound_form, 'detail':detail})

class ListDelete(View):
	def get(self, request, slug):
		detail = List.objects.get(slug__iexact=slug)
		return render(request, 'qr_list/qr_delete.html', context={'detail':detail})		
		
	def post(self, request, slug):
		detail = List.objects.get(slug__iexact=slug)
		detail.delete()
		return redirect(reverse('base_page'))