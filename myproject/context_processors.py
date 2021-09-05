from django.conf import settings

def recaptcha(request):
    return {
        'recaptcha_enabled': settings.GOOGLE_RECAPTCHA_ENABLED,
        'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
    }
