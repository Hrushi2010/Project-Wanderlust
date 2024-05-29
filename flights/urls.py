# from django.urls import path
# from . import views

# urlpatterns = [
#     path('search/', views.search_flights, name='search_flights'),
#     path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
#     # other paths
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # Other URL patterns...
#     path('search/', views.search_flights, name='search_flights'),
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.search_flights, name='search_flights'),
#     path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
# ]

# # flights/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.search_flights, name='search_flights'),
#     path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
#     path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
#     path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
# ]


# # flights/urls.py

# from django.urls import path
# from . import views

# app_name = 'flights'

# urlpatterns = [
#     path('', views.flight_list, name='flight_list'),
#     path('search/', views.search_flights, name='search_flights'),
#     path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
#     path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
# ]

# # flights/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.flight_list, name='flight_list'),
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.flight_list, name='flight_list'),
#     path('search/', views.search_flights_view, name='search_flights_view'),
# ]


# flights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('search/', views.search_flights_view, name='search_flights_view'),
]

# flights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('search/', views.search_flights_view, name='search_flights_view'),
]

# flights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('search/', views.search_flights_view, name='search_flights_view'),
]
