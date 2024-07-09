from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # routes all urls to views
    path('admin/', admin.site.urls),
    path('', include('home.urls')),     # uses all urlpatterns in home app
    path('neat/', include('notes.urls')),       # uses all urlpatterns in notes app
]
