from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notepad.urls')),
    path('finance/', include('finance.urls')),
    path('news_list/', include('news_list.urls')),
    path('newsscraper/', include('news_Scraper.urls')),
    path('dashapp/', include('dash_app.urls')),
]
