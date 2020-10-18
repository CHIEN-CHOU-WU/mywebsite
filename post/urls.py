from django.urls import path

from . import views
urlpatterns = [
	path('', views.listpost_view.as_view(), name="post"),
	path('details/<int:pk>', views.detailpost_view.as_view(), name="post-details"),   # pk = primarykey
	path('add_post/', views.addpost_view.as_view(), name="post-add"),
]