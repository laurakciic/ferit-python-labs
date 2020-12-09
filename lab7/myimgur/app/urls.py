from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:image_id>/', views.detail, name='detail'),
    path('<int:image_id>/comment', views.comment, name='comment'),
]
