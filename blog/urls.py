from django.urls import path
from . import views

urlpatterns = [
    path('api/posts/', views.PostListView.as_view(), name='post-list'),
    path('api/posts/<int:id>/', views.PostDetailView.as_view(), name='post-detail'),
    
]
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
