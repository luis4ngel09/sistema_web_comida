#from django.shortcuts import render
from django.utils import timezone
from .models import comidas,pedidos
from .forms import comidaForm,pedidoForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='usuario/login/')
def index(request):
	return render(request, 'comida/base.html')

@login_required(login_url='usuario/login/')
def comida_list(request):
	comida = comidas.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
	return render(request, 'comida/comida_list.html', {'comidas':comida})

@login_required(login_url='usuario/login/')
def comidaDetalle(request,pk):
	comida = get_object_or_404(comidas, pk=pk)
	return render(request, 'comida/comidaDetalle.html', {'comida': comida})

@login_required(login_url='usuario/login/')
def comidaEditaqr(request,pk):
	comida = get_object_or_404(comidas, pk=pk)
	if request.method == "POST":
		form = comidaForm(request.POST, request.FILES, instance=comida)
		if form.is_valid():
			comidas = form.save(commit=False)
			comidas.author = request.user
			comidas.save()
		return redirect('comidaDetalle', pk=pk)
	else:
		form = comidaForm(instance=comida)
	return render(request, 'comida/comidaNueva.html', {'form': form})

@login_required(login_url='usuario/login/')
def comidaEditar(request, pk):
	post = get_object_or_404(comidas, pk=pk)
	if request.method == "POST":
		form = comidaForm(request.POST,request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('comidaDetalle', pk=post.pk)
	else:
		form = comidaForm(instance=post)
	return render(request, 'comida/comidaNueva.html', {'form': form})

@login_required(login_url='usuario/login/')
def comidaNueva(request):
	if request.method=='POST':
		form = comidaForm(request.POST, request.FILES)
		if form.is_valid():
			comidas = form.save(commit=False)
			comidas.author = request.user
			comidas.save()
			return redirect('comidaDetalle', pk=comidas.pk)
			#return render_to_response()
	else:
		form=comidaForm()
	return render(request,'comida/comidaNueva.html',{'form':form})

@login_required(login_url='usuario/login/')
def pedidoNew(request):
	#pedido = get_object_or_404(pedidos, pk=comida.pk)
	if request.method=='POST':
		form = pedidoForm(request.POST)
		if form.is_valid():
			pedido = form.save(commit=False)
			pedido.author = request.user
			pedido.save()
			return redirect('principal')
			#return render_to_response()
	else:
		form=pedidoForm()
	return render(request,'comida/pedidoNew.html',{'form':form})

@login_required(login_url='usuario/login/')
def pedidoList(request):
	pedido = pedidos.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
	return render(request, 'comida/pedidoList.html', {'pedidos':pedido})

@login_required(login_url='usuario/login/')
def pedidoEditar(request, pk):
	post = get_object_or_404(pedidos, pk=pk)
	if request.method == "POST":
		form = pedidoForm(request.POST,request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('principal')
	else:
		form = pedidoForm(instance=post)
	return render(request, 'comida/pedidoNew.html', {'form': form})


def usuarioLogin(request):
	if not request.user.is_anonymous():
		return redirect('index')
	if request.method == 'POST':
		#formulario = AuthenticationForm(request.POST)
		usuario=request.POST['username']
		clave= request.POST['password']
		acceso = authenticate(username=usuario,password=clave)
		if acceso is not None:
			if acceso.is_active:
				login(request,acceso)
				return redirect('index')
			else:
				msg1= 'USUARIO NO ACTIVO!!'
				return render(request, 'comida/login.html', {'msg': msg1})
		else:
			msg1= 'NO EXISTE!!'
			return render(request, 'comida/login.html', {'msg': msg1})
	else:
		return render(request, 'comida/login.html')
	return render(request, 'comida/login.html')

@login_required(login_url='usuario/login/')
def userNew(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			render(request, 'comida/login.html')
	else:
		formulario = UserCreationForm()
	return render_to_response('comida/new_user.html',{'formulario':formulario},content_type=None)

#@login_required(login_url='usuario/login/')
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
	