from django.forms import ModelForm
from app1.models import customer

class customerForm(ModelForm):
	class Meta:
		model=customer
		fields=['c_id','c_name']