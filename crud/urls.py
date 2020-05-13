from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url,include
from crud import settings
from ppp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('data/',views.data, name="data"),
    path('intex/',views.intex),
    path('data/<int:id>/update/',views.update, name="update"),
    path('data/<int:id>/delete/', views.delete , name="delete"),
    path('data/<int:id>/item/', views.item , name="item"),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

