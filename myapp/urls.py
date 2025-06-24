# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('base/' , views.base,name='base'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('blog/', views.blog, name='blog'),  # blog page
    path('contact/', views.contact, name='contact'),  # contact page
    path('gallery/', views.gallery, name='gallery'),  # gallery page
    path('bird-netting-services/', views.birdnettingservices, name='bird-netting-services'),  # bird-netting-services page
    path('bird-spike-system/', views.birdspikesystem, name='bird-spike-system'),  # bird-netting-services page
    path('sport-net/', views.sportnet, name='sport-net'),  # bird-netting-services page
    path('car-parking-net-system/', views.carparkingnetsystem, name='car-parking-net-system'),  # bird-netting-services page
    path('swimming-pool-protect-net-system/', views.swimmingpool, name='swimming-pool-protect-net-system'),  # bird-netting-services page
    path('safety-nets/', views.safetynet, name='safety-nets'),  # bird-netting-services page
    path('exploring-the-essential-role-of-bird-netting-services-in-effective-bird-damage-management/', views.exploring, name='exploring-the-essential'),  # bird-netting-services page
    path('designing-ethically-optimizing-videos-and-shining-the-spotlight-on-our-smashingconf-speakers/', views.Keepingpigeons, name='Keeping-Pigeons'),  # bird-netting-services page
    path('flowing-excellence-dripping-perfection-your-plumbers-of-choice/', views.pleatedpigeon, name='pleated-pigeon'),  # bird-netting-services page
    path('tags/spikes/', views.spikes, name='spikes'),  # bird-netting-services page
    path('tags/bird/', views.bird, name='bird'),  # bird-netting-services page
]
