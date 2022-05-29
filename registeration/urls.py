from django.urls import path
from . import views


urlpatterns = [
    path('', views.Grad, name='Grad'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('user/', views.user, name='user'),
    path('forgot/', views.forgotpass, name='forgotpass'),
    path('welcome2/', views.welcome2, name='welcome2'),
    path('log/', views.log, name='log'),
    path('processes/', views.processes, name='processes'),
    path('rna/', views.rna, name='rna'),
    path('dna/', views.dna, name='dna'),
    path('protein/', views.protein, name='protein'),
    path('profile/', views.profile, name='profile'),

]
