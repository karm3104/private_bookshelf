import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z)o&pdappd)a$w2u2(r1j!w_6*(#3rtfc#4$!ag_vv^0$7(6r1'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bookshelf.apps.BookshelfConfig',
    'accounts.apps.AccountsConfig',
    
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.google',

    'django_ses'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'private_bookshelf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "config", "templates"),
                os.path.join(BASE_DIR, "config", 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'private_bookshelf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# データベース設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'private_bookshelf',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',    # 管理サイト用(ユーザー名認証)
    'allauth.account.auth_backends.AuthenticationBackend',  #一般ユーザー用(メールアドレス認証)
)

#ACCOUNT_AUTHENTICATION_METHOD = 'email'   # email+パスワード認証方式を指定
ACCOUNT_USERNAME_REQUIRED = True         # Falseでユーザ名を利用しない設定にする

SITE_ID = 1   #django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別用IDを設定
LOGIN_REDIRECT_URL = 'bookshelf:book_list'   # ログインURLの設定
# LOGIN_REDIRECT_URL = 'home'   # ログインURLの設定
LOGIN_URL = '/accounts/login/'   #ログイン画面を何処にするかの設定
ACCOUNT_LOGOUT_REDIRECT_URL = 'bookshelf:index'   #ログアウトリダイレクトの設定
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'   #ユーザ登録確認メールを送信する
ACCOUNT_EMAIL_REQUIRED = True    #メールアドレスを必須項目に指定

ACCOUNT_LOGOUT_ON_GET = True     #ログアウトリンクのクリック一発でログアウトする設定

ACCOUNT_EMAIL_SUBJECT_PREFIX = ''   #django-allauthが送信するメールの件名に自動付与される接頭辞をブランクにする設定
DEFAULT_FROM_EMAIL = 'mbshelf@gmail.com'   #デフォルトのメール送信元を設定


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #コンソール上にメッセージを表示

MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}

# バックアップバッチ用
BACKUP_PATH = 'backup/'
NUM_SAVED_BACKUP = 30


