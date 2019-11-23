from django import forms
from . models import List
from django.core.exceptions import ValidationError
from django.utils import timezone


class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ['qr_quantity','qr_name', 'qr_city', 'qr_campaign', 'qr_source', 'qr_product',]
		
	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		return new_slug

