from django.urls import path
from . import views

urlpatterns = [

    path('', views.all_articles, name='allarticles'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('Guestinfo/', views.Guestinfo, name='Guestinfo'),
    path('login/', views.login, name='login'),
    path('submit/', views.submit, name='submit'),
    path('logout/', views.logout, name='logout'),
]
