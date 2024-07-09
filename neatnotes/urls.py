from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Routes all urls to views
    path('admin/', admin.site.urls),
    path('', include('home.urls')),     # Uses all urlpatterns in home app
    path('neat/', include('notes.urls')),       # Uses all urlpatterns in notes app
]
