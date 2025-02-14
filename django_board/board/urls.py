from django.urls import path
from . import views

urlpatterns = [
    
    path('users/',views.users_list, name="user_board"),
    path('users/new_user',views.user_add, name="add_user"),
    path('users/<str:name>',views.user_view, name="view_user"),
    path('users/<str:name>/edit',views.user_edit, name="edit_user"),
    path('users/<str:name>/delete',views.user_delete,name="delete_user")
]