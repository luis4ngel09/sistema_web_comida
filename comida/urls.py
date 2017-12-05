from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
	#url(r'^$', views.comida_list,name='principal' ),
	url(r'index/$', views.index,name='index' ),
	url(r'inicio/$', views.comida_list,name='principal' ),
	url(r'^$',views.usuarioLogin,name='usuarioLogin'),
	#url(r'^$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name="login"),
	url(r'^cerrar/$', views.logout_view, name="logout"),
	url(r'usuario/nuevo/$', views.userNew, name='userNew'),
	url(r'usuario/login/$',views.usuarioLogin,name='usuarioLogin'),
	url(r'comida/nueva/$',views.comidaNueva,name='comidaNueva'),
	url(r'pedido/new/$',views.pedidoNew,name='pedidoNew'),
	url(r'pedidos/list/$',views.pedidoList,name='pedidoList'),
	url(r'^pedido/(?P<pk>[0-9]+)/$', views.pedidoEditar, name='pedidoEditar'),
	url(r'^comida/(?P<pk>[0-9]+)/$', views.comidaDetalle, name='comidaDetalle'),
	url(r'^comida/(?P<pk>[0-9]+)/editar/$', views.comidaEditar, name='comidaEditar'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)