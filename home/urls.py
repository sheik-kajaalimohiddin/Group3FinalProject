from django.urls import path, re_path
from .views import login_view, logout_view, register_view, home_view, event_view, profile_view, listing_view, \
    detail_view, enquire_view
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'home'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('event/', event_view, name='event'),
    path('add_event/', views.add_event, name='add_event'),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/enquire/', enquire_view, name='enquire'),
    path('listings/', listing_view, name='listings'),
    path('listings/details/<int:pk>/', detail_view, name='details'),
    path('add_property/', views.add_property, name='add_property'),
    path('edit_property/<int:pk>/', views.edit_property, name='edit_property'),
    path('', home_view, name='home'),
    path('search/', views.property_search, name='property_search'),
    path('report/', views.generate_report, name='generate_report'),
    path('remove_listing/<int:property_id>/', views.remove_listing, name='remove_listing'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
