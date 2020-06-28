from settings.local import *


SEND_EMAILS = False

DATABASES["default"]["TEST"] = {
    "NAME": "tonis_piip_org_test",
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
