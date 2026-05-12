from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 SEGURIDAD (DESARROLLO)
SECRET_KEY = 'django-insecure-cambia-esto-por-una-clave-tuya'

DEBUG = True

ALLOWED_HOSTS = []


# 📦 APLICACIONES INSTALADAS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 👇 tu app
    'empleados',
]


# ⚙️ MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 🌐 URL PRINCIPAL
ROOT_URLCONF = 'biometrico_web.urls'


# 🎨 PLANTILLAS (IMPORTANTE)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # puedes dejarlo vacío si usas templates dentro de la app
        'APP_DIRS': True,  # 🔥 IMPORTANTE (esto carga login.html y demás)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 🗄 BASE DE DATOS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔑 VALIDACIONES DE USUARIOS
AUTH_PASSWORD_VALIDATORS = []


# 🌍 INTERNACIONALIZACIÓN
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# 📁 ARCHIVOS ESTÁTICOS
STATIC_URL = 'static/'


# 🔐 LOGIN / LOGOUT (IMPORTANTE PARA TU SISTEMA)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'


# 🔥 AUTO PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'