"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sto import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),

    url(r'^sto/sign-in/$', auth_views.login,
        {'template_name': 'sto/sign_in.html'},
        name='sto-sign-in'),

    url(r'^sto/sign-out', auth_views.logout,
        {'next_page': '/'},
        name='sto-sign-out'),

    url(r'^sto/$', views.sto_home, name='sto-home'),

    url(r'^sto/sign-up', views.sto_sign_up, name='sto-sign-up'),

    url(r'^sto/account/$', views.sto_account, name='sto-account'),

    url(r'^sto/services/$', views.sto_services, name='sto-services'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
