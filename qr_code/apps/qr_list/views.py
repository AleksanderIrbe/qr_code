from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from . forms import ListForm
from . models import List
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse
# импортируется модуль сосздания QR кода
import qrcode, os
# из модуля обработки изображений импортируется конвертер форматов
from PIL import Image

# для отображения списка QR кодов. Тут может быть дополнительный функционал с пагинацией страниц и с 
# возможностью вернуться на страницу, с которой происходило редактирование QR кода. Но в задании этого не было
def base_page(request):
	latest_list = List.objects.all()
	return render(request, 'qr_list/qr_list.html', {'latest_list':latest_list})

# для генерации изображения QR кода
class ListDetail(View):
	def get(self, request, slug):
		detail = get_object_or_404(List, slug__iexact=slug)
		# задаются параметры внешнего вида QR кода
		qr = qrcode.QRCode(
		    version=1, # размер от 1 до 40
		    error_correction=qrcode.constants.ERROR_CORRECT_L, # Степень корректировки ошибок L,M,Q,H
		    box_size=10, # количество пикселов в клеточке
		    border=4, # толщина рамки
		)
		# задается путь к папке, в которой хранятся графические файлы 
		img_path = os.path.abspath('./qr_code/static/qr_list/')
		
		# формируется содержимое QR кода. В нашем случае - адрес страницы 
		# промежуточного шлюза со слагом идентичным слагу в базе
		# можно записать туда и еще всякую информацию, но для простоты - только слаг
		qr_slug = self.slug__iexact=slug
		# поля передаются в переменную data
		data = ('http://127.0.0.1:8000/qr/code/' + qr_slug)
		# переменная присваивается функции QR кода
		qr.add_data(data)
		qr.make(fit=True)
		# задается цвет QR кода и фона
		img = qr.make_image(fill_color="black", back_color="white")
		#задается имя и тип. Для упрощения предполагается, что генерируются QR коды
		#в один момент и сразу скачиваются. Поэтому используется статическое имя файла
		#который перезаписывается при каждой следующей генерации
		#filename = self.slug__iexact=slug + '.png'
		filename = 'qr.png'
		# QR код сохраняется в формате png
		img.save(os.path.join(img_path, filename))
		# файл в формате png передается в конвертер
		path_open = img_path +'/' + filename
		j_file = Image.open(path_open)
		# сохраняется в нужных форматах
		j_file.save(os.path.join(img_path, 'qr.jpg'))
		j_file.save(os.path.join(img_path, 'qr.pdf'))
		return render(request, 'qr_list/qr_detail.html', {'detail':detail, 'img_path':img_path})

# для создания записи в список QR кодов
class ListCreate(View):
	def get(self, request):
		#вызывается форма, в которой можно внести исходные данные. 
		#Дата и время устанавливаются автоматически, слаг сгенерирован из названия и времени
		form=ListForm()
		return render(request, 'qr_list/qr_create.html', {'form':form})

	def post(self, request):
		bound_form=ListForm(request.POST)
		#Если внесенные данные валидны, открывается список QR кодов
		if bound_form.is_valid():
			new_qr=bound_form.save()
			return redirect(reverse('base_page'))
		#Если данные с ошибкой, открывается форма с указаниями на ошибки
		return render(request, 'qr_list/qr_create.html', {'form':bound_form})

# для изменения сохраненного QR кода
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

#для удаления QR кода
class ListDelete(View):
	def get(self, request, slug):
		detail = List.objects.get(slug__iexact=slug)
		return render(request, 'qr_list/qr_delete.html', context={'detail':detail})		
		
	def post(self, request, slug):
		detail = List.objects.get(slug__iexact=slug)
		detail.delete()
		return redirect(reverse('base_page'))

# для промежуточного шлюза
class IntermediateGate(View):
	def get(self, request, slug):
		#здесь поставлено возвращение ошибки 404, которая возникнет, если вводится QR код записи, которую уже удалили.
		# но можно добавить проверку и выдавать таким посетителям переход на какую-нибудь другую целевую страницу.
		detail = get_object_or_404(List, slug__iexact=slug)
		#счетчик берет значение из базы, прибавляет единицу и отправляет обратно в базу.
		#Могут быть самые разные варианты: подсчет в логах, обращение к сторонним сервисам, введение фильтров от накруток
		quantity = int(detail.qr_quantity) + 1
		detail = List.objects.get(slug__iexact=slug)
		detail.qr_quantity = quantity
		detail.save()
		return render(request, 'qr_list/qr_intermediate.html', context={'quantity':quantity})