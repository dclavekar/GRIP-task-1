from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),
    path('payment/',views.payment,name="payment"),
    path('success/',views.success, name="success"),
    path('razor/',views.razor,name='razor')
    
]
urlpatterns += staticfiles_urlpatterns()