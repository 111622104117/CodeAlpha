from django.contrib import admin
from django.urls import path, include
from social import views as social_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', social_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
