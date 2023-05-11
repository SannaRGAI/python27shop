from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, FavoriteViewSet, AddRatiingAPIView



router = DefaultRouter()
router.register('comment',CommentViewSet)
router.register('favorites',FavoriteViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('rating/', AddRatiingAPIView.as_view())
]