from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    # 회원가입
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("<int:user_pk>/", views.detail, name="detail"),
    # 로그인 / 로그아웃
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/follow/", views.follow, name="follow"),
]
