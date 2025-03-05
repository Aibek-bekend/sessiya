from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('thread_list')),  # Басты бет /threads-ке бағыттайды
    path('', include('posts.urls')),
]
