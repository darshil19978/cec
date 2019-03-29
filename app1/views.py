from django.shortcuts import render
from app1.forms import customerForm
# Create your views here.
def home(Request):
	return render(Request,"app1/home.html")

def registration(Request):
	forms=customerForm()
	context={
		'form':forms
	}
	return render(Request,"app1/registration.html",context)