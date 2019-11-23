from django import forms
from . models import List
from django.core.exceptions import ValidationError
from django.utils import timezone


class ListForm(forms.ModelForm):
	class Meta:
		model = List
		#fields = ['qr_quantity','qr_name', 'qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'slug',]
		fields = ['qr_quantity','qr_name', 'qr_city', 'qr_campaign', 'qr_source', 'qr_product',]
		#widgets = {'qr_quantity':forms.TextInput(attrs={'value':0})}
			

		

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == "create":
			#raise ValidationError('Нельзя использовать слаг "create", он уже занят.')
			new_slug = new_slug + '-1'
		if List.objects.filter(slug__iexact=new_slug).count():
			count = List.objects.filter(slug__iexact=new_slug).count()
			new_slug = new_slug + '-' + str(int(count))
			#raise ValidationError('Нельзя использовать слаг  "{}" , он уже занят'.format(new_slug))

		return new_slug

	# def save(self):
	# 	new_list = List.objects.create(qr_name = self.cleaned_data['qr_name'],
	# 									qr_city = self.cleaned_data['qr_city'],
	# 									qr_campaign = self.cleaned_data['qr_campaign'],
	# 									qr_source = self.cleaned_data['qr_source'],
	# 									qr_product = self.cleaned_data['qr_product'],
	# 									slug = self.cleaned_data['slug'],
	# 									#qr_date = self.cleaned_data['qr_date'],
	# 									qr_quantity = self.cleaned_data['qr_quantity'],
	# 									)
	# 	return new_list
		

		



# class ListForm(forms.ModelForm):
# 	class Meta:
# 		model = List
# 		fields = ['qr_name', 'qr_city', 'qr_campaign', 'qr_source', 'qr_product', 'qr_quantity']
	

