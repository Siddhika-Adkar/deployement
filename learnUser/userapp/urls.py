from django.urls import path
from userapp import views

from django.conf import settings
from django.conf.urls.static import static

app_name='userapp'
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('img/',views.gallery,name='img'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
