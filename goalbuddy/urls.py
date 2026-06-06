# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     path("accounts/", include('accounts.urls')),
#     path("dashboard/", include('dashboard.urls')),
#     path("goal/", include('goal.urls')),
#     path("", include('home.urls')),
#     path("interview/", include('interview.urls')),

# ]

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),  
    path('goal/', include('goal.urls')),
    path('', include('home.urls')),
    path('interview/', include('interview.urls')),
]