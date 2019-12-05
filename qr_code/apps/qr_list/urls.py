from django.urls import path
from qr_list import views

urlpatterns = [
# на список QR кодов
    path('', views.base_page, name='base_page'), 
# на страницу создания QR кода
    path('create/', views.ListCreate.as_view(), name='qr_create_url'),
# на страницу сгенерированного QR ода
    path('<str:slug>/', views.ListDetail.as_view(), name='qr_detail_url'),
# на страницу изменения
    path('<str:slug>/update/', views.ListUpdate.as_view(), name='qr_update_url'),
# на страницу удаления 
    path('<str:slug>/delete/', views.ListDelete.as_view(), name='qr_delete_url'),
# на промежуточный шлюз
    path('code/<str:slug>/', views.IntermediateGate.as_view(), name='intermediate_gate'),
        ]