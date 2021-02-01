from django.urls import path
from . import views
urlpatterns = [
    path('',views.todo_list, ),
    path('create/', views.todo_create,),
    path('<id>/',views.todo_detail, ),
    path('<id>/update/',views.todo_update, ),
    path('<id>/delete/',views.todo_delete,),
]
