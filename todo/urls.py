from django.urls import path

from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo_list_url'),
    path('create/', views.TodoCreate.as_view(), name='todo_create_url'),
    path('<str:slug>/', views.TodoDetail.as_view(), name='todo_detail_url'),
    path('<str:slug>/update/', views.TodoUpdate.as_view(), name='todo_update_url'),
    path('<str:slug>/delete/', views.TodoDelete.as_view(), name='todo_delete_url'),
]
