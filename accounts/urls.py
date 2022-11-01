from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:pk>/', views.mypage_1, name='mypage_1'),
    path('<int:pk>/', views.mypage_2, name='mypage_2'),
]