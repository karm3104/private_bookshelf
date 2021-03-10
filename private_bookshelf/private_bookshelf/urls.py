from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static

from . import settings_common, settings_dev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),
    path('accounts/', include('allauth.urls')),
]

# 開発サーバーでメディアを配信できるようにする設定
urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)

# # DEBUG TOOL BAR の設定
# if settings_dev.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
