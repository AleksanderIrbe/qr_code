from django.contrib import admin
from . models import List
#from datetime import datetime
#from Time import time

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
	# порядок отображения полей
	#list_display = ('qr_name', 'qr_date',  'qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'qr_quantity', 'qr_create')
	#prepopulated_fields = {'slug':('qr_name', 'qr_city' )}
	list_display = ('qr_name', 'qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'slug')
    
	# поля, которые можно сразу редактировать
	#list_editable = ('qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'qr_quantity')
	# поля, по которым возможна фильтрация
	#list_filter = ('qr_name','qr_date',  'qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'qr_quantity')
	#date_hierarchy = 'qr_date'
	
	# создаем переменную qr_create отвечающую в которую передаем данные для генерации QR кода
	def qr_create(self,request):
		qr_create = "<a href='#'>создаем</a>"
		return qr_create