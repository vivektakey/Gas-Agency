from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('tsq/',views.Tsq,name='tsq'),
    path('track/',views.track,name='track'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),





]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    