from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'main'

# Une seule liste avec segments traduisibles
urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),

    # Pages statiques (segments traduits via fichiers .po)
    path(_('qui-sommes-nous/') , views.about, name='about'),
    path(_('nos-procedes/'), views.processes, name='processes'),
    path(_('nos-produits/'), views.products, name='products'),
    path(_('qualite/'), views.quality, name='quality'),
    path(_('contact/'), views.contact, name='contact'),

    # Offres d'emploi
    path(_('recrutement/'), views.recruitment, name='recruitment'),
    path(_('recrutement/<str:job_name>/'), views.recruitment_job_name, name='recruitment_job_name'),

    # Pages supplémentaires
    path(_('mentions-legales/'), views.legal, name='legal'),
    path(_('politique-de-protection-des-donnees/'), views.privacy, name='privacy'),
    path(_('politique-des-cookies/'), views.cookies, name='cookies'),
]
