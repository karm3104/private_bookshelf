from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    'version': 1,  # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'bookshelf': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# #DEBUG TOOL BAR の設定
# if DEBUG:
#     def show_toolbar(request):
#         return True

# INSTALLED_APPS += (
#     'debug_toolbar',
# )
# MIDDLEWARE += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK' : show_toolbar,
# }
