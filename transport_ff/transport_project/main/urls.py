from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('car-list/', views.CarListView.as_view(), name='car_list'),
    path('car-detail/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('book/new', views.BookCreateView.as_view(), name='book_new'),
    path('book/detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('book/list', views.BookListView.as_view(), name='book_list'),
    path('book/edit/<int:pk>', views.BookUpdateView.as_view(), name='book_edit'),
    path('book/delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete'),
    path('ride/new', views.RideCreateView.as_view(), name='ride_new'),
    path('ride/detail/<int:pk>', views.RideDetailView.as_view(), name='ride_detail'),
    path('ride/list', views.RideListView.as_view(), name='ride_list'),
    path('ride/edit/<int:pk>', views.RideUpdateView.as_view(), name='ride_edit'),
    path('ride/delete/<int:pk>', views.RideDeleteView.as_view(), name='ride_delete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

