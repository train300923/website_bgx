from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import os


class Page(models.Model):
    """
    Modèle pour les pages du site (accueil, à propos, services, etc.)
    """
    # Identifiant unique pour la page
    slug = models.SlugField(
        _('Slug'),
        max_length=100,
        unique=True,
        help_text=_('URL de la page (ex: accueil, a-propos)')
    )

    # Titre de la page
    title_fr = models.CharField(_('Titre (Français)'), max_length=200)
    title_en = models.CharField(_('Titre (Anglais)'), max_length=200)

    # Contenu de la page
    content_fr = models.TextField(_('Contenu (Français)'), blank=True)
    content_en = models.TextField(_('Contenu (Anglais)'), blank=True)

    # Métadonnées SEO
    meta_description_fr = models.CharField(
        _('Meta Description (Français)'),
        max_length=160,
        blank=True
    )
    meta_description_en = models.CharField(
        _('Meta Description (Anglais)'),
        max_length=160,
        blank=True
    )

    # Image principale de la page
    main_image = models.ImageField(
        _('Image principale'),
        upload_to='pages/',
        blank=True,
        help_text=_('Image principale de la page')
    )

    # Ordre d'affichage dans le menu
    menu_order = models.PositiveIntegerField(
        _('Ordre dans le menu'),
        default=0,
        help_text=_('Ordre d\'affichage dans le menu principal')
    )

    # Page visible ou non
    is_published = models.BooleanField(_('Publiée'), default=True)

    # Date de création et modification
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')
        ordering = ['menu_order', 'title_fr']
    def __str__(self):
        return self.title_fr


class ContactMessage(models.Model):
    """
    Modèle pour les messages de contact
    """
    # Informations du contact
    name = models.CharField(_('Nom'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Téléphone'), max_length=20, blank=True)
    company = models.CharField(_('Entreprise'), max_length=100, blank=True)

    # Message
    subject = models.CharField(_('Sujet'), max_length=200)
    message = models.TextField(_('Message'))

    # CV uploadé (optionnel)
    cv_file = models.FileField(
        _('CV'),
        upload_to='cvs/',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])],
        help_text=_('Formats acceptés: PDF, DOC, DOCX (max 5MB)')
    )

    # Type de contact
    CONTACT_TYPES = [
        ('commercial', _('Demande commerciale')),
        ('candidature', _('Candidature')),
        ('information', _('Demande d\'information')),
        ('autre', _('Autre')),
    ]
    contact_type = models.CharField(
        _('Type de contact'),
        max_length=20,
        choices=CONTACT_TYPES,
        default='information'
    )

    # Statut du message
    STATUS_CHOICES = [
        ('new', _('Nouveau')),
        ('read', _('Lu')),
        ('replied', _('Répondu')),
        ('archived', _('Archivé')),
    ]
    status = models.CharField(
        _('Statut'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    # Date de réception
    received_at = models.DateTimeField(_('Reçu le'), auto_now_add=True)

    class Meta:
        verbose_name = _('Message de contact')
        verbose_name_plural = _('Messages de contact')
        ordering = ['-received_at']

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.received_at.strftime('%d/%m/%Y')})"

    def clean(self):
        """Validation personnalisée"""
        if self.cv_file:
            # Vérifier la taille du fichier (5MB max)
            if self.cv_file.size > 5 * 1024 * 1024:
                raise ValidationError(_('Le fichier CV ne doit pas dépasser 5MB.'))


class JobOffer(models.Model):
    """
    Modèle pour les offres d'emploi
    """
    # Informations de base
    title_fr = models.CharField(_('Titre (Français)'), max_length=200)
    title_en = models.CharField(_('Titre (Anglais)'), max_length=200)

    # Description
    description_fr = models.TextField(_('Description (Français)'))
    description_en = models.TextField(_('Description (Anglais)'))

    # Détails
    location = models.CharField(_('Lieu'), max_length=100)
    contract_type = models.CharField(
        _('Type de contrat'),
        max_length=50,
        choices=[
            ('cdi', _('CDI')),
            ('cdd', _('CDD')),
            ('stage', _('Stage')),
            ('freelance', _('Freelance')),
        ]
    )

    # Salaire (optionnel)
    salary_min = models.PositiveIntegerField(_('Salaire minimum'), blank=True, null=True)
    salary_max = models.PositiveIntegerField(_('Salaire maximum'), blank=True, null=True)

    # Statut
    is_published = models.BooleanField(_('Publiée'), default=True)
    is_featured = models.BooleanField(_('Mise en avant'), default=False)

    # Dates
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)
    application_deadline = models.DateField(_('Date limite de candidature'), blank=True, null=True)

    class Meta:
        verbose_name = _('Offre d\'emploi')
        verbose_name_plural = _('Offres d\'emploi')
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title_fr


class SiteConfiguration(models.Model):
    """
    Configuration générale du site (informations de contact, etc.)
    """
    # Informations de l'entreprise
    company_name = models.CharField(_('Nom de l\'entreprise'), max_length=200)
    company_email = models.EmailField(_('Email de contact'))
    company_phone = models.CharField(_('Téléphone'), max_length=20)
    company_address = models.TextField(_('Adresse'))

    # Réseaux sociaux
    linkedin_url = models.URLField(_('LinkedIn'), blank=True)
    twitter_url = models.URLField(_('Twitter'), blank=True)

    # Configuration email
    contact_email = models.EmailField(
        _('Email pour les contacts'),
        help_text=_('Email qui recevra les messages du formulaire de contact')
    )

    # Logo
    logo = models.ImageField(_('Logo'), upload_to='config/', blank=True)

    class Meta:
        verbose_name = _('Configuration du site')
        verbose_name_plural = _('Configurations du site')

    def __str__(self):
        return f"Configuration - {self.company_name}"

    def save(self, *args, **kwargs):
        # S'assurer qu'il n'y a qu'une seule configuration
        if not self.pk and SiteConfiguration.objects.exists():
            raise ValidationError(_('Une seule configuration est autorisée.'))
        super().save(*args, **kwargs)
