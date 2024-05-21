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


from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_flights, name='search_flights'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
]
