from settings.base import *


DEBUG = False

# fmt: off
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=["tonis-piip-org.test.tonis.piip.org"]
)
# fmt: on

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = env.str("DJANGO_SITE_URL", default="https://tonis-piip-org.test.tonis.piip.org")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

EMAIL_HOST = env.str("DJANGO_EMAIL_HOST", default="smtp.sparkpostmail.com")
EMAIL_PORT = env.int("DJANGO_EMAIL_PORT", default=587)
EMAIL_HOST_USER = env.str("DJANGO_EMAIL_HOST_USER", default="SMTP_Injection")
EMAIL_HOST_PASSWORD = env.str("DJANGO_EMAIL_HOST_PASSWORD", default="TODO (api key)")

STATIC_URL = env.str("DJANGO_STATIC_URL", default="/assets/")

# Production logging - all INFO and higher messages go to info.log file. ERROR and higher messages additionally go to
#  error.log file plus to Sentry.
LOGGING["handlers"] = {
    "sentry": {
        "level": "ERROR",
        "class": "raven.contrib.django.raven_compat.handlers.SentryHandler",
    },
}

LOGGING["loggers"][""] = {
    "handlers": ["console", "sentry"],
    "level": "INFO",
    "filters": ["require_debug_false"],
}

if env.str("DJANGO_DISABLE_FILE_LOGGING", default="n") != "y":
    # Add file handlers as addition to sentry
    LOGGING["handlers"].update(
        {
            "info_log": {
                "level": "INFO",
                "class": "logging.handlers.WatchedFileHandler",
                "filename": "/var/log/tonis_piip_org/info.log",
                "formatter": "default",
            },
            "error_log": {
                "level": "ERROR",
                "class": "logging.handlers.WatchedFileHandler",
                "filename": "/var/log/tonis_piip_org/error.log",
                "formatter": "default",
            },
        }
    )
    LOGGING["loggers"][""]["handlers"] = ["info_log", "error_log", "sentry"]

else:
    LOGGING["handlers"].update(
        {"console": {"class": "logging.StreamHandler", "formatter": "default"}}
    )

# Sentry error logging
INSTALLED_APPS += ("raven.contrib.django.raven_compat",)
RAVEN_BACKEND_DSN = env.str(
    "DJANGO_RAVEN_BACKEND_DSN", default="https://TODO:TODO@sentry.thorgate.eu/TODO"
)
RAVEN_PUBLIC_DSN = env.str(
    "DJANGO_RAVEN_PUBLIC_DSN", default="https://TODO@sentry.thorgate.eu/TODO"
)
RAVEN_CONFIG["dsn"] = RAVEN_BACKEND_DSN

# Enable S3 storage
DEFAULT_FILE_STORAGE = "tonis_piip_org.storages.MediaStorage"
MEDIA_ROOT = env.str("DJANGO_MEDIA_ROOT", default="")
AWS_STORAGE_BUCKET_NAME = env.str(
    "DJANGO_AWS_STORAGE_BUCKET_NAME", default="tonis_piip_org-staging"
)
AWS_ACCESS_KEY_ID = env.str("DJANGO_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("DJANGO_AWS_SECRET_ACCESS_KEY")
