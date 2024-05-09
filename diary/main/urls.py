from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary, name='diary_list'),
    path('forum/', views.forum, name='forum'),
    path('create/', views.create_note, name='create_note'),
    path('<int:pk>', views.ViewNote.as_view(), name='view_note'),
    path('<int:pk>/update', views.UpdateNote.as_view(), name='update_note'),
    path('<int:pk>/delete', views.DeleteNote.as_view(), name='delete_note'),
]
