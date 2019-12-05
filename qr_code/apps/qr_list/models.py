from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

# слаг создается из названия QR кода. С помощью slugify преобразуется в нижний регистр и вычищается
# но slugify работает только с латиницей, другим языкам нужно сделать транслитерацию
# Для простоты установлена транслитерация только для русского языка
def latinizator(letter, dic):
		for i, j in dic.items():
			letter = letter.replace(i, j)
		return letter
#в момент сохранения в эту функцию будет передано назвение QR кода и сгенерируется слаг
def gen_slug(s):
	rus_slug = slugify(s, allow_unicode=True)
	#транслитерация
	legend = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'y','ы':'y','ь':"'",'э':'e','ю':'yu','я':'ya',}
	new_slug = latinizator(rus_slug, legend)
	#функция возвращает транслитерированный слаг, к которому добавлено количество секунд, прошедших с 1970г
	#таким образом обеспечивается уникальность. Можно добавить дополнительные проверки уникальности, 
	#но для простоты оставлено так
	return new_slug + '-' + str(int(time()))
	

class List(models.Model):
	qr_date = models.DateTimeField('дата создания', auto_now_add=True, db_index=True)
	qr_name = models.CharField('Название QR кода', max_length=100, null=False, blank=True, db_index=True)
	qr_city = models.CharField('City', max_length=100, null=False, blank=True, )
	qr_campaign = models.CharField('Campaign', max_length=100, null=False, blank=True, )
	qr_source = models.CharField('Source', max_length=100, null=False, blank=True, )
	qr_product = models.CharField('Product', max_length=100, null=False, blank=True, )
	qr_quantity = models.IntegerField('счетчик', default=0, null=False, blank=True)
	slug = models.SlugField('слаг', unique=True, blank=True)
#сортировка списка по хронологии
	class Meta:
		ordering = ('-qr_date',)

	def get_absolute_url(self):
		return reverse('qr_detail_url', kwargs={'slug':self.slug})

	def get_update_url(self):
		return reverse('qr_update_url', kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('qr_delete_url', kwargs={'slug':self.slug})

	def get_detail_url(self):
		return reverse('qr_detail_url', kwargs={'slug':self.slug})
#при сохранении проверяется наличие id. Если его нет, значит запись сохраняется впервые и нужно сгенерировать слаг
#если id есть, значит сохраняется уже имеющийся слаг
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.qr_name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.qr_name