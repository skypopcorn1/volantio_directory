from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^team/([a-z0-9-]+)/$', views.team_member_detail, name = 'team_member_detail' ),
	url(r'^team/([a-z0-9-]+)/edit/$', views.edit, name = 'edit' )
]