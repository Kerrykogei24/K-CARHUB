from django.conf.urls import url,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    url(r'^$',views.index,name='home'),
    url(r'^logout/$',views.logout_request,name="logout"),
    path('postImage/', views.post_image, name='postImage'),
    path('photos', views.photos, name='photos'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('single_art/<art_id>', views.single_car, name='single-car'),
    path('unfollow/<user_id>', views.unfollow, name='unfollow'),
    path('follow/<user_id>', views.follow, name='follow'),
    



]