__author__ = 'mrk2'
"""url configuration"""

from django.conf.urls import patterns, url

from blog.views import detail
# from blog.views import index


urlpatterns = patterns(  # pylint: disable=invalid-name
    '',
    #url(r'^$', index, name='Index'),
    url(r'(?P<slug>[\w-]+)', detail, name='detail'),
    url(r'^$', "blog.views.indexblog", name='ndx'),
)