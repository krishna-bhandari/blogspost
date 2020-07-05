
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import job.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',job.views.home,name='home'),
    path('blogs/', include('blog.urls')),
    path('profile/', include('job.urls')),

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)