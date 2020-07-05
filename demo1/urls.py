from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet


router = routers.DefaultRouter()
router.register('books', BookViewSet)
urlpatterns = [
   # path('', views.first),
    path('', include(router.urls))
    #path('first_class', first_class.as_view()),
    
]
