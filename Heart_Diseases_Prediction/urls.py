from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('Predict/', include('Predict.urls')),
    path('admin/', admin.site.urls),
] 
