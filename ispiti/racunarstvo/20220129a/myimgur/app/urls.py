from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:image_id>/', views.detail, name='detail'),
    path('<int:image_id>/comment', views.comment, name='comment'),
    path('<int:image_id>/like_comment/<int:comment_id>', views.likebtn, name = 'likebtn'),
    path('<int:comment_id>/approve' ,views.approve, name = 'approve'),
    path('<int:image_id>/upvote', views.upvote, name='upvote'),
    path('<int:image_id>/downvote', views.downvote, name='downvote'),
    path('new', views.create_image, name="create_image"),
    path('random', views.random_image, name="random_image"),
    path('<int:image_id>/edit', views.update_image, name="edit_image"),
    path('<int:image_id>/delete', views.delete_image, name="delete_image"),
    
]
