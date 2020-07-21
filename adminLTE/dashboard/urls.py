from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='company-details'),
    path('edit-offer/', views.edit_offer, name='edit-offer'),
    path('add-offer/', views.add_offer, name='add-offer'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('password/', views.enterPassword, name='enterPassword'),
]
   