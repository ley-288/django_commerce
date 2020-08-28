from django import forms

from.models import Product


class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
					widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	email 		=forms.EmailField()
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
									"placeholder": "Your title",
									"class": "new-class-name two",
									"id": "my-id-for-textarea",
									"rows": 20,
									"cols": 120
								}
							)
						)
	price		= forms.DecimalField(initial=199.99)
	
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if "CFE" in title:
			return title
		else:
			raise forms.ValidationError("This is not a valid title")
		#or if not in title.. raise forms..... return title. Then we can add multiple validations

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("title")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email

class RawProductForm(forms.Form):
	title 		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
									"placeholder": "Your title",
									"class": "new-class-name two",
									"id": "my-id-for-textarea",
									"rows": 20,
									"cols": 120
								}
							)
						)
	price		= forms.DecimalField(initial=199.99)