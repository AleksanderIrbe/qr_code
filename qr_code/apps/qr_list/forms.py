from django import forms
from . models import List
from django.core.exceptions import ValidationError
from django.utils import timezone

class ListForm(forms.Form):
	#qr_date = forms.DateTimeField(auto_now_add=True)
	#qr_date = forms.DateTimeField()
	qr_quantity = forms.IntegerField()

	qr_name = forms.CharField(max_length=100)
	qr_city = forms.CharField(max_length=100)
	qr_campaign = forms.CharField(max_length=100)
	qr_source = forms.CharField(max_length=100)
	qr_product = forms.CharField(max_length=100)
	slug = forms.SlugField(max_length=600)

	#qr_date.widget.attrs.update({'class':'form-control', 'value':timezone.now()})
	qr_quantity.widget.attrs.update({'class':'form-control', 'value':0})
	#qr_quantity.widget.attrs.update({'class':'form-control'})
	qr_name.widget.attrs.update({'class':'form-control'})
	qr_city.widget.attrs.update({'class':'form-control'})
	qr_campaign.widget.attrs.update({'class':'form-control'})
	qr_source.widget.attrs.update({'class':'form-control'})
	qr_product.widget.attrs.update({'class':'form-control'})
	slug.widget.attrs.update({'class':'form-control'})

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == "create":
			raise ValidationError('Нельзя использовать слаг "create", он уже занят.')
		if List.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('Нельзя использовать слаг  "{}" , он уже занят'.format(new_slug))

		return new_slug

	def save(self):
		new_list = List.objects.create(qr_name = self.cleaned_data['qr_name'],
										qr_city = self.cleaned_data['qr_city'],
										qr_campaign = self.cleaned_data['qr_campaign'],
										qr_source = self.cleaned_data['qr_source'],
										qr_product = self.cleaned_data['qr_product'],
										slug = self.cleaned_data['slug'],
										#qr_date = self.cleaned_data['qr_date'],
										qr_quantity = self.cleaned_data['qr_quantity'],
										)
		return new_list
		

		



# class ListForm(forms.ModelForm):
# 	class Meta:
# 		model = List
# 		fields = ['qr_name', 'qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'qr_quantity']
	

