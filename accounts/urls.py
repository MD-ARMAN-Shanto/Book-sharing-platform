from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    #path('login', views.login_user, name='login'),
    #path('logout', views.logout_user, name='logout'),
    #path('user', views.user_view, name='user'),

    path('user/profile', views.book_form, name='list'),
    path('user/upload', views.book_create, name='create'),
    path('profile/update/<int:id>', views.update_view, name='update'),
    path('profile/<int:id>', views.delete_view, name='delete'),
    path('profile/detail/<int:id>', views.book_details, name='details')




]