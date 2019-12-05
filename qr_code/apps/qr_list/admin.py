from django.contrib import admin
from . models import List
#from datetime import datetime
#from Time import time

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
	# порядок отображения полей
	list_display = ('qr_name', 'qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'slug')
    
    #Можно при желании добавить функционал, который легко реализуется в админке:
	# поля, которые можно редактировать в таблице
	#list_editable = ('qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'qr_quantity')
	# поля, по которым возможна фильтрация
	#list_filter = ('qr_name','qr_date',  'qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'qr_quantity')
	#date_hierarchy = 'qr_date'