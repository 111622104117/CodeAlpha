from django.contrib import admin
from django.urls import path, include
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', store_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout
    path('', include('store.urls')),
]
