from .view import BlogPostRudView, BlogPostAPIView

from django.conf.urls import url

urlpatterns =[
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name ='post-rud'),
    url(r'^$', BlogPostAPIView.as_view(), name ='post-listcreate')
]
