from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name="home"),
    path('addngo/', views.addngo,name="addngo"),
    path('addngos/', views.addngos,name="addngos"),
    path('addngos/addngos/', views.addngos,name="addngos"),
    path('search', views.search,name="serach"),
    path('cityload', views.cityload,name="cityload"),
    path('finalshow', views.finalshow,name="finalshow"),
    path('viewdetails', views.viewdetails,name="viewdetails"),
    path('review', views.review,name="review"),
    path('reviews', views.reviews,name="reviews"),
]
