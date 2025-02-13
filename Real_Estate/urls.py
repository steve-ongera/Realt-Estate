
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views

admin.site.site_header = 'Estate Admin'
admin.site.index_title = 'Admin page'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', include('listings.urls')),
    path('', include('pages.urls')),
    path('realtors/', include('realtors.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contacts/', include('contacts.urls')),
    path('register/', views.account_view, name='account-user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/account-user_login.html'),
         name='account-user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/account-user_logout.html'),
         name='account-user_logout'),
]

if settings.DEBUG:
         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
