from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('tom/srt=a2864O8YN8KPUxl', views.qr_code),
    path('tom/srt=a2864O9YN8KPUxl', views.qr_code_1),
    path('tom/srt=a286410YN8KPUxl', views.qr_code_2),
]