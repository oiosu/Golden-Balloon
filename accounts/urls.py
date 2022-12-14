from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage_1/<int:pk>/', views.mypage_1, name='mypage_1'),
    path('update/', views.update, name='update'),
    path('mypage_2/<int:pk>/', views.mypage_2, name='mypage_2'),
    path('<int:pk>/follow/', views.follow, name='follow'),
]