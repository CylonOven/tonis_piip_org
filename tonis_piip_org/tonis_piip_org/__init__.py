from tonis_piip_org.celery import app as celery_app


default_app_config = "tonis_piip_org.apps.TonisPiipOrgConfig"

__all__ = ["celery_app"]
