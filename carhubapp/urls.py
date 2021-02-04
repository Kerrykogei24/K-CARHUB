from django.conf.urls import url,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import FlashcardDeleteView

urlpatterns=[
    path('', views.index, name='index'),
    url(r'^logout/$',views.logout_request,name="logout"),
    path('about/', views.about, name='about'),
    path('postImage/', views.post_image, name='postImage'),
    path('photos', views.photos, name='photos'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('single_art/<art_id>', views.single_car, name='single-car'),
    path('unfollow/<user_id>', views.unfollow, name='unfollow'),
    path('follow/<user_id>', views.follow, name='follow'),
    path('post/<int:pk>/delete/',FlashcardDeleteView.as_view(), name="deleteForm"),
    



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
