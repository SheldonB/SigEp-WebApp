from django.shortcuts import render_to_response

# Create your views here.
def index(request):
	return render_to_response('index.html')

def bms(request):
	return render_to_response('bms.html')

def contact(request):
	return render_to_response('contact.html')