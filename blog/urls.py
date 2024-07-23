from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
] # The second slug variable could be any name. The first is the data type.
# as_view() not required in function based views