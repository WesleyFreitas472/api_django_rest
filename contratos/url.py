from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'estado/$',views.EstadoView.as_view()),
        url(r'estado/(?P<pk>[0-9]+)/$', views.EstadoDetail.as_view()),
        
        url(r'cidade/$',views.CidadeView.as_view()),

]


