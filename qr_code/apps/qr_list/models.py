from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
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

	class Meta:
		ordering = ('-qr_date',)

	def get_absolute_url(self):
		return reverse('qr_detail_url', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.qr_name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.qr_name