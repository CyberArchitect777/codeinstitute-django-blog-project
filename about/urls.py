from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
    #path('<slug:slug>/', views.post_detail, name='post_detail'),
] # The second slug variable could be any name. The first is the data type.
# as_view() not required in function based views