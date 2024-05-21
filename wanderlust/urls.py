# """
# URL configuration for wanderlust project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.contrib import admin
# from django.urls import path
# from flights import views as flight_views
# from hotels import views as hotel_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('flights/', flight_views.search_flights, name='search_flights'),
#     path('hotels/', hotel_views.search_hotels, name='search_hotels'),
# ]

# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('flights/', include('flights.urls')),
#     path('hotels/', include('hotels.urls')),
#     path('payments/', include('payments.urls')),
# ]


# wanderlust/urls.py

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('flights/', include('flights.urls')),  # Assuming you have a separate urls.py file in the flights app
#     path('hotels/', include('hotels.urls')),    # Assuming you have a separate urls.py file in the hotels app
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('flights/', include('flights.urls')),
#     path('hotels/', include('hotels.urls')),
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', include('hotels.urls')),
]
