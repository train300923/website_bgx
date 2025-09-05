from django.urls import path
from django.utils.translation import get_language
from . import views

app_name = 'main'

# URLs françaises (par défaut)
urlpatterns_fr = [
    # Page d'accueil
    path('', views.home, name='home'),
 
    # Pages statiques
    path('qui-sommes-nous/', views.about, name='about'),
    path('nos-procedes/', views.processes, name='processes'),
    path('nos-produits/', views.products, name='products'),
    path('qualite/', views.quality, name='quality'),
    path('contact/', views.contact, name='contact'),
 
    # Offres d'emploi
    path('recrutement/', views.recruitment, name='recruitment'),
    path('recrutement/<str:job_name>/', views.recruitment_job_name, name='recruitment_job_name'),
 
    # Pages supplémentaires
    path('mentions-legales/', views.legal, name='legal'),
    path('politique-de-protection-des-donnees/', views.privacy, name='privacy'),
    path('politique-des-cookies/', views.cookies, name='cookies'),
]

# URLs anglaises (traduites)
urlpatterns_en = [
    # Page d'accueil
    path('', views.home, name='home'),
 
    # Pages statiques (traduites)
    path('about-us/', views.about, name='about'),
    path('our-processes/', views.processes, name='processes'),
    path('our-products/', views.products, name='products'),
    path('quality/', views.quality, name='quality'),
    path('contact/', views.contact, name='contact'),
 
    # Offres d'emploi
    path('recruitment/', views.recruitment, name='recruitment'),
    path('recruitment/<str:job_name>/', views.recruitment_job_name, name='recruitment_job_name'),
 
    # Pages supplémentaires
    path('legal-notice/', views.legal, name='legal'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('cookie-policy/', views.cookies, name='cookies'),
]

# URLs par défaut (français)
urlpatterns = urlpatterns_fr
