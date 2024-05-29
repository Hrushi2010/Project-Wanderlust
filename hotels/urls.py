# from django.urls import path
# from . import views

# urlpatterns = [
#     path('search/', views.search_hotels, name='search_hotels'),
#     path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
#     # other paths
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.search_hotels, name='search_hotels'),
#     path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_hotels, name='search_hotels'),
    path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('booking/success/', views.booking_success, name='booking_success'),
]


