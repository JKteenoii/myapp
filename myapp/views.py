from django.shortcuts import render

def index(request):
	return render(request, 'index.html')


def menu1(request):
	return render(request, 'menu1.html')

def menu2(request):
	return render(request, 'menu2.html')

def menu3(request):
	return render(request, 'menu3.html')

def myself(request):
	return render(request, 'myself.html')