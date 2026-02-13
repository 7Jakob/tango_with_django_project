from django.contrib import admin
from django.urls import path, include
from rango import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),

]
