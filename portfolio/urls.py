from django.conf.urls.static import static
from django.urls import path, include
from .views import home_view, AboutListView, ContactView, PortfolioListView

urlpatterns = [
    path('', home_view, name='index-page'), 
    path('about/', AboutListView.as_view(), name='about-page'), 
    path('contact/', ContactView.as_view(), name='contact-page'), 
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-page'), 
]