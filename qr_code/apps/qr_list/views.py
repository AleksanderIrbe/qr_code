from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from . forms import ListForm
from . models import List
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse
# импортируется модуль сосздания QR кода
import qrcode
# из модуля обработки изображений импортируется конвертер форматов
from PIL import Image

# Create your views here.
# на главной странице для отображения таблицы
def base_page(request):
	latest_list = List.objects.all()
	admin_url = '../admin/qr_list/list/'
	return render(request, 'qr_list/qr_list.html', {'latest_list':latest_list, 'admin_url':admin_url,})
	

class ListDetail(View):
	def get(self, request, slug):
		detail = get_object_or_404(List, slug__iexact=slug)
				# задаются параметры внешнего вида
		qr = qrcode.QRCode(
		    version=1, # размер от 1 до 40
		    error_correction=qrcode.constants.ERROR_CORRECT_L, # Степень корректировки ошибок L,M,Q,H
		    box_size=10, # количество пикселов в клеточке
		    border=4, # толщина рамки
		)

		# набор полей таблицы. В работающем варианте должны вводиться из базы данных
		qr_slug = self.slug__iexact=slug
		# поля передаются в переменную data
		data = (qr_slug)
		# переменная присваивается функции QR кода
		qr.add_data(data)
		qr.make(fit=True)
		# задается цвет QR кода и фона
		img = qr.make_image(fill_color="black", back_color="white")
		#задается имя и тип 
		name = self.slug__iexact=slug + '.png'
		# QR код сохраняется в формате png
		img.save(name)
		# файл в формате png передается в конвертер
		# j_file = Image.open(img)

		# # сохраняется в нужных форматах
		# j_file.save('3.jpg')
		# j_file.save('3.pdf')


		return render(request, 'qr_list/qr_detail.html', {'detail':detail, 'img':img})

class ListCreate(View):
	def get(self, request):
		form=ListForm()
		return render(request, 'qr_list/qr_create.html', {'form':form})

	def post(self, request):
		bound_form=ListForm(request.POST)
		if bound_form.is_valid():
			new_qr=bound_form.save()
			return redirect(reverse('base_page'))
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


class ListCode(View):
	def qr_code_generator(self, request, slug):
		qr_link = 'photo.irbe.pro'
		data = (qr_link + self.slug)
		# переменная присваивается функции QR кода
		qr.add_data(data)
		qr.make(fit=True)
		# задается цвет QR кода и фона
		img = qr.make_image(fill_color="black", back_color="white")
		# QR код сохраняется в формате png
		img_name = self.slug + '.png'
		img.save(img_name)
		return img.png


	def get(self, request, slug):
		detail = List.objects.get(slug__iexact=slug)
		bound_form = ListForm(instance=detail)
		return render(request, 'qr_list/qr_code.html', context={'form':bound_form, 'detail':detail})
