from django.conf.urls import url
from . import views

app_name = 'castingShop'
urlpatterns = [
    url(r'^$',views.Home.as_view(),name='home'),
    url(r'^product/(?P<slug>[-\w]+)/$', views.ProductDetailView.as_view(), name='product'),
    url(r'^customize/$',views.CustomizeView,name='customize')
]
