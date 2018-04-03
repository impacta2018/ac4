# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return render(request, "index.html")

@csrf_exempt
def contato(request):
	if request.method == "GET":
		print("Acesso via GET")
		return render(request, "contato.html")
	else:
		print("Acesso via POST\n")

		name = request.POST.get("name")
		email = request.POST.get("email")
		password = request.POST.get("password")
		sexo = request.POST.get("sexo")
		est = request.POST.get("est")
		obs = request.POST.get("obs")

		print(
			"Name: " + name + "\n" +
			"Email: " + email + "\n" +
			"Password: " + password + "\n" +
			"Sexo: " + sexo + "\n" +
			"Estado: " + est + "\n" +
			"Observações: " + obs + "\n"
		)

@csrf_exempt
def login(request):
	print("request", request)
	print("method", request.method)
	if request.method == "GET":
		print("Acesso via GET")
		return render(request, "login.html")
	else:		 
		print("Acesso via POST\n")

		email = request.POST.get("email")
		password = request.POST.get("password")

		if password == "teste123":
			msg = "Usuário " + email + " entrou com sucesso!"
			to = "index.html"
		else:
			msg = "Usuário " + email + " digitou a senha errada!"
			to = "login.html"

		print(msg + "\n")		
		# return HttpResponse(msg)
		return render(request, to)
	