# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from contas.backend import *

def entrar(request):
    context = {}
    if request.method == "POST":
        if autenticar(request):
            return redirect("/")
        else:
            context["erro"] = "Problemas no login"
    return render(request, "index.html", context)

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

		post = [str(name),' ',str(email),' ',str(password),' ',str(sexo),' ',str(est),' ',str(obs)]

		# for i in post:
		# 	print(i)

		msg = ''.join(post)

		print(msg)
		return HttpResponse(msg)

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
	