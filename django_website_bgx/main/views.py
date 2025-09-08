from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from .models import Page, JobOffer, SiteConfiguration


def home(request):
    """Page d'accueil"""
    try:
        home_page = Page.objects.get(slug='accueil')
    except Page.DoesNotExist:
        home_page = None
    
    # Récupérer les offres d'emploi mises en avant
    featured_jobs = JobOffer.objects.filter(is_featured=True, is_published=True)[:3]
    
    # Configuration du site
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': home_page,
        'featured_jobs': featured_jobs,
        'config': config,
    })


def about(request):
    """Page Qui sommes-nous / About Us"""
    page = get_object_or_404(Page, slug='qui-sommes-nous', is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': page,
        'config': config,
    })


def processes(request):
    """Page Nos procédés / Our Processes"""
    page = get_object_or_404(Page, slug='nos-procedes', is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': page,
        'config': config,
    })


def products(request):
    """Page Nos produits / Our Products"""
    page = get_object_or_404(Page, slug='nos-produits', is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': page,
        'config': config,
    })


def quality(request):
    """Page Qualité / Quality"""
    page = get_object_or_404(Page, slug='qualite', is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': page,
        'config': config,
    })


def contact(request):
    """Page Contact"""
    page = get_object_or_404(Page, slug='contact', is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': page,
        'config': config,
    })


def recruitment(request):
    """Page Recrutement / Recruitment"""
    jobs = JobOffer.objects.filter(is_published=True).order_by('-is_featured', '-created_at')
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'jobs': jobs,
        'config': config,
    })


def recruitment_job_name(request, job_name):
    """Détail d'une offre d'emploi par nom"""
    # Convertir le nom en slug pour la recherche
    job_slug = job_name.replace('-', ' ').lower()
    job = get_object_or_404(JobOffer, title_fr__icontains=job_slug, is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'job': job,
        'config': config,
    })


def legal(request):
    """Page Mentions légales / Legal Notice"""
    page = get_object_or_404(Page, slug='mentions-legales', is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': page,
        'config': config,
    })


def privacy(request):
    """Page Politique de protection des données / Privacy Policy"""
    page = get_object_or_404(Page, slug='politique-de-protection-des-donnees', is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': page,
        'config': config,
    })


def cookies(request):
    """Page Politique des cookies / Cookie Policy"""
    page = get_object_or_404(Page, slug='politique-des-cookies', is_published=True)
    config = SiteConfiguration.objects.first()
    
    return render(request, 'main/page.html', {
        'page': page,
        'config': config,
    })
