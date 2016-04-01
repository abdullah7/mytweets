from django.conf.urls import include, url
from django.contrib import admin
from tweets.views import Index, Profile, PostTweet, HashTagCloud

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mytweets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # index
    url(r'^$', Index.as_view()),

    # /user/
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^user/(\w+)/post/$', PostTweet.as_view()),

    # /hashtag/
    url(r'^hashtag/(\w+)/$', HashTagCloud.as_view()),

    # /admin/
    url(r'^admin/', include(admin.site.urls)),
]
