"""KoloRESTApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_auth.registration.views import SocialAccountListView, \
    SocialAccountDisconnectView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf.urls.static import static

from RESTApi.views import IndexTemplateView
from . import settings
from rest_framework_swagger.views import get_swagger_view
from RESTApi import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'profile_links', views.ProfileViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'file_set', views.FileSet)
router.register(r'hardware_rentals', views.HardwareRentalSet)
router.register(r'hardwares', views.HardwareSet)
router.register(r'project', views.ProjectSet)
router.register(r'section', views.SectionSet)
router.register(r'gallery', views.GallerySet)

schema_view = get_swagger_view(title='SKNI KOD Website API')

urlpatterns = [
    url(r'^$', IndexTemplateView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/github/$', views.GitHubLogin.as_view(), name='github_login'),
    url(r'^rest-auth/github/connect/$', views.GitHubConnect.as_view(), name='github_connect'),
    url(
        r'^socialaccounts/$',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    url(
        r'^socialaccounts/(?P<pk>\d+)/disconnect/$',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    ),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^obtain-token/', TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    url(r'^verify-token/', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^users/$', views.UserViewSetList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>\d+)/$', views.UserViewSetDetail.as_view(), name='user_detail'),
    url(r'^groups/$', views.GroupViewSetList.as_view(), name='group_list'),
    url(r'^groups/(?P<pk>\d+)/$', views.GroupViewSetDetail.as_view(), name='group_detail'),
    url(r'^docs$', schema_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
