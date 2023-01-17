from django import forms
from .models import Respon, Responses

class ResponCreateForm(forms.ModelForm):
	
	class Meta:
		model = Respon
		fields = ['tag', "patterns"]

class ResponsesCreateForm(forms.ModelForm):
	
	class Meta:
		model = Responses
		fields = ['tag','responses']
