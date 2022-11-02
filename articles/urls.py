from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
    path("c_create/<int:pk>", views.c_create, name="c_create"),
    path("c_delete/<int:a_pk>/<int:c_pk>", views.c_delete, name="c_delete"),
    path("like/<int:pk>", views.like, name="like"),
    path("notice/", views.notice, name="notice"),
    path("n_create/", views.n_create, name="n_create"),
    path("n_detail/<int:pk>", views.n_detail, name="n_detail"),
    path("n_delete/<int:pk>", views.n_delete, name="n_delete"),
    path("n_update/<int:pk>", views.n_update, name="n_update"),
    path("reviews/", views.reviews, name="reviews"),
    path("reviews/create", views.r_create, name="r_create"),
    path("reviews/<int:pk>", views.r_detail, name="r_detail"),
    path("reviews/delete/<int:pk>", views.r_delete, name="r_delete"),
    path("reviews/update/<int:pk>", views.r_update, name="r_update"),
    path("reviews/c_create/<int:pk>", views.r_c_create, name="r_c_create"),
    path("reviews/c_delete/<int:a_pk>/<int:c_pk>", views.r_c_delete, name="r_c_delete"),
]
