from django.urls import path
#from . import views 
from qr_list import views
#from .views import *




#app_name = 'qr_list'

urlpatterns = [
    path('', views.base_page, name='base_page'), 
    path('create/', views.ListCreate.as_view(), name='qr_create_url'),
    path('<str:slug>/', views.ListDetail.as_view(), name='qr_detail_url'),
    path('<str:slug>/update/', views.ListUpdate.as_view(), name='qr_update_url'),
    path('<str:slug>/delete/', views.ListDelete.as_view(), name='qr_delete_url'),
    path('code/<str:slug>/', views.IntermediateGate.as_view(), name='intermediate_gate'),
    #path('code/<str:slug>/', views.intermediate, name='intermediate_gate'),
        ]

