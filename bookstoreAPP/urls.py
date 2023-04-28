from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Local
    path('user', include('accounts.urls')),
    path('', include('pages.urls')),
]
