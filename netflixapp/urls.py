from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('profiles', views.ProfileList.as_view(), name='profile_list'),
    path('profile-create', views.ProfileCreate.as_view(), name='profile-create'),
    # جلب ايدي البروفايل في الرابط
    path('watch/<str:profile_id>', views.MovieList.as_view(), name='movie-list'),
    path('watch/detail/<str:movie_id>', views.MovieDetail.as_view(), name='movie-detail'),
    path('watch/paly/<str:movie_id>', views.PlayMovie.as_view(), name='play-movie'),
]
