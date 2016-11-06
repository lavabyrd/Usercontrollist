from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.CustomerView.as_view(),
        name='customers'
    ),
]
