from django.conf import settings
import requests

def recaptcha_is_valid(request):
    if settings.GOOGLE_RECAPTCHA_ENABLED:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        return result['success']
    return True
