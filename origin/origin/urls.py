from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from django.urls import path, re_path, include
from bonds.views import BondView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bonds/', BondView.as_view()),
    re_path('bonds/(?P<legal_name>.+)/$', BondView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_then_login)
]
