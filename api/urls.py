from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'acordo/$',views.AcordoCreate.as_view()),
	url(r'acordos/$',views.AcordoList.as_view()),
	url(r'acordo/(?P<pk>[0-9]+)/$', views.AcordoDetail.as_view()),


	url(r'cliente/$',views.ClienteCreate.as_view()),
	url(r'clientes/$',views.ClienteList.as_view()),
	url(r'cliente/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view()),
	url(r'cliente/edit/(?P<pk>[0-9]+)/$', views.ClienteUpdate.as_view()),
	url(r'cliente/delete/(?P<pk>[0-9]+)/$', views.ClienteDelete.as_view()),

	url(r'parcela/$',views.ParcelaCreate.as_view()),
	url(r'parcela/edit/(?P<pk>[0-9]+)/$', views.ParcelaUpdate.as_view()),
	url(r'parcela/delete/(?P<pk>[0-9]+)/$', views.ParcelaUpdate.as_view()),
	

]
