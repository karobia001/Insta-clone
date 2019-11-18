from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views
# from django.urls import path, re_path


urlpatterns=[
    url(r'^$', views.timeline, name='allTimelines'),
    url(r'^profile/', views.find_profile, name='find_profile'),
    url(r'^image/(\d+)', views.single_image, name='singleImage'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)