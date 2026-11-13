import os
SECRET_KEY = os.environ.get("SECRET_KEY", "solo-desarrollo-local-serie4")
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]
INSTALLED_APPS = ["django.contrib.contenttypes", "rest_framework", "corsheaders", "animales"]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware", "django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "config.urls"
DATABASES = {"default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": os.environ.get("DB_NAME", "serie4_animales"),
    "USER": os.environ.get("DB_USER", "serie4"),
    "PASSWORD": os.environ.get("DB_PASSWORD", ""),
    "HOST": os.environ.get("DB_HOST", "127.0.0.1"),
    "PORT": os.environ.get("DB_PORT", "3307"),
    "OPTIONS": {"charset": "utf8mb4"}
}}
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "UNAUTHENTICATED_USER": None
}
CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]
LANGUAGE_CODE = "es"
TIME_ZONE = "America/Guatemala"
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
