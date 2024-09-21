
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from contact.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contact', include('contact.urls')),
    path('api/fact', include('factcard.urls')),
    path('api/review', include('review.urls')),
    path('', IndexView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)