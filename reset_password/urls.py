from django.conf.urls import patterns, include, url
from django.contrib import admin
from utils.views import ResetPasswordRequestView, PasswordResetConfirmView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reset_password.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


)
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^account/reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
                       # PS: url above is going to used for next section of implementation.
                       url(r'^account/reset_password', ResetPasswordRequestView.as_view(), name="reset_password"),
                       )