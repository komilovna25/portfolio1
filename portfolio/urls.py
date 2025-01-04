from django.conf.urls.static import static
from django.urls import path, include
from .views import home_view, AboutListView,ServicesListView,ContactView,ResumeListView,PortfolioListView,Category
from  .import views

urlpatterns = [
    path('', home_view, name='hero-page'), 
    path('about/', AboutListView.as_view(), name='about-page'), 
    path('contact/', ContactView.as_view(), name='contact-page'), 
    path('resume/', ResumeListView.as_view(), name='resume-page'), 
    path('services/', ServicesListView.as_view(), name='services-page'), 
    path('Category/', views.Category, name='Category'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-page'), 
 
]