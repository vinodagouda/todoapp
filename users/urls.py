from django.urls import path
from users import views as user

urlpatterns = [
    path('', user.user_login, name="user_login"),
    path('logout/', user.user_logout, name="user_logout"),
    path('sign-up/',user.user_signup, name="user_signup"),
]