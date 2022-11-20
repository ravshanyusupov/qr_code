from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('2864O8YN8KPUxl/', views.qr_code),
]