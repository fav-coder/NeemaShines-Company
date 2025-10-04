from django.urls import path
from. import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('create_service/', views.create_service, name='create_service'),
    path('update_service/<int:pk>/', views.update_service, name='update_service'),
    path('delete_service/<int:pk>/', views.delete_service, name='delete_service'),
    path('booking/', views.booking, name='booking'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('update_booking/<int:pk>/', views.update_booking, name='update_booking'),
    path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('join_us/', views.join_us, name='join_us'),
    path('contact/', views.contact, name='contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)