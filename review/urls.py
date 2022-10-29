from django.urls import path
from . import views


app_name = "review"

urlpatterns = [
    # review 게시글
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:review_pk>/", views.detail, name="detail"),
    path("<int:review_pk>/update/", views.update, name="update"),
    path("<int:review_pk>/delete/", views.delete, name="delete"),
    # comment
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path(
        "<int:review_pk>/comments/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path(
        "<int:review_pk>/comments/<int:comment_pk>/update/",
        views.comment_update,
        name="comment_update",
    ),
    path(
        "<int:review_pk>/comments/<int:comment_pk>/update/complete/",
        views.comment_update_complete,
        name="comment_update_complete",
    ),
    path("<int:review_pk>/like/", views.like, name="like"),
    path("search/", views.search, name="search"),
]
