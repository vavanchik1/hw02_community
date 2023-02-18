from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
