from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('list/', views.list),
    path('store/<int:store_id>', views.all)]



